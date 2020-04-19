from django.urls import path ,include
from .views import Blog_Post_list
urlpatterns = [
    path('<int:pk>/',Blog_Post_list.as_view(),name="details"),
    path('',Blog_Post_list.as_view(),name="creat_detail"),
]