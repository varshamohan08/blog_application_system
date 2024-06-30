from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Blog
from .serializers import BlogSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
import logging
logger = logging.getLogger(__name__)
from blog_application_system import ins_logger
from sys import exc_info


# Create your views here.
class BlogPagination(PageNumberPagination):
    page_size = 10

class ListBlogsAPI(APIView):
    def get(self, request):
        try:
            # import pdb;pdb.set_trace()
            query = request.GET.get('query', '')
            blogs = Blog.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).order_by('-publication_date')
            
            paginator = BlogPagination()
            result_page = paginator.paginate_queryset(blogs, request)
            serializer = BlogSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e),"success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BlogsAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # import pdb;pdb.set_trace()
            pk = request.GET.get('pk')
            if pk:
                blog = get_object_or_404(Blog, pk=pk)
                serializer = BlogSerializer(blog)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                blogs = Blog.objects.filter(author = request.user)
                serializer = BlogSerializer(blogs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e),"success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        # import pdb;pdb.set_trace()
        try:
            serializer = BlogSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({"success":True, 'details': serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"success":False, 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e),"success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            # import pdb;pdb.set_trace()
            blog = get_object_or_404(Blog, pk=request.data.get('id'))
            if blog.author == request.user:
                serializer = BlogSerializer(blog, data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response({"success":True, 'details': serializer.data}, status=status.HTTP_200_OK)
                return Response({"success":False, 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"deatils": "Blog created by different author"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e),"success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            blog = get_object_or_404(Blog, pk=request.data.get('id'))
            if blog.author == request.user:
                blog.delete()
                return Response({"deatils": "Blog deleted successfully", "success":True}, status=status.HTTP_200_OK)
            return Response({"deatils": "Blog created by different author", "success":False}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e), "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
