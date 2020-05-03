from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .user_view import UserApi as user



urlpatterns = [

    path('',user.as_view()),
]







