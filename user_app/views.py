from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.contrib.auth.models import User
from .serializers import UserSerializer
import logging
logger = logging.getLogger(__name__)
from blog_application_system import ins_logger
from sys import exc_info

{
    "email":"user1@test.com",
    "password":"test@123"
}

class userLogin(APIView):
    def post(self, request):
        try:
            username = request.data.get('email', None)
            password = request.data.get('password', None)
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                user_details = {
                    'username': user.username,
                    'email': user.email
                }
                return Response({"success":True, 'details': 'Success', 'access_token': access_token, 'userdetails': user_details}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False, 'details': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e),"success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
class userLogout(APIView):
    def get(self, request):
        logout(request)
        return Response({'detail': 'Success'}, status=status.HTTP_200_OK)
{
    "email":"user1@test.com",
    "password":"test@123",
    "first_name":"user",
    "last_name":"1"
}
class userSignUp(APIView):
    def post(self, request):
        try:
            # import pdb;pdb.set_trace()
            with transaction.atomic():
                user_serializer = UserSerializer(data=request.data)
                
                if user_serializer.is_valid():
                    username = request.data.get('email')
                    user = User.objects.create_user(
                        username=username,
                        email=request.data.get('email'),
                        password=request.data.get('password'),
                        first_name=request.data.get('first_name'),
                        last_name=request.data.get('last_name')
                    )

                    user_details = {
                        'username': user.username,
                        'email': user.email
                    }
                    return Response({"success":True, 'userdetails': user_details}, status=status.HTTP_200_OK)
                return Response({"success":False, 'details': user_serializer.errors}, status=status.HTTP_200_OK)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e),"success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class userApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            if request.GET.get('id'):
                user_instance = User.objects.filter(id=request.GET.get('id')).values().first()
            else:
                user_instance = User.objects.values()
            return Response({"success":True, 'userdetails': user_instance}, status=status.HTTP_200_OK)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e),"success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request):
        try:
            id = request.data
            User.objects.filter(id = id).delete()
            return Response({"success":True}, status = status.HTTP_200_OK)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e),"success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request):
        try:
            user_id = request.data.get('id')
            user_instance = User.objects.get(id=user_id)
            
            user_serializer = UserSerializer(instance=user_instance, data=request.data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({"success":True, 'details': user_serializer.data}, status=status.HTTP_200_OK)
            
            return Response({"success":False, 'details': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e),"success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        try:
            current_password = request.data['current_password']
            new_password = request.data['new_password']

            user = request.user
            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                return Response({"success":True}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False, 'details': 'Current password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # logging the specific error into log/error.log file
            exc_type, exc_value, exc_traceback = exc_info()
            ins_logger.logger.error(str(e), extra={'details':'line no: ' + str(exc_traceback.tb_lineno)})
            return Response({"details":str(e),"success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
