from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogsAPI.as_view(), name='blog_api'),
    path('list', ListBlogsAPI.as_view(), name='list'),
]