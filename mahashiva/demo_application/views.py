#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from .models import Blog_Post
from .serializers import Blog_PostSerializer
from django.contrib.auth.models import User


# Create your views here.
class Blog_Post_list(APIView):
    def get_object(self,slug):
        try:
            return Blog_Post.objects.get(slug=slug)
        except:
            return Response.status_code(status.HTTP_404_NOT_FOUND)

    def get(self,request,slug):
        serializer=Blog_PostSerializer(self.get_object(slug),many=True)
        return Response.status_code(serializer.data)

    def post(self,request):
        account=User.objects.get(id=4)
        blog_post=Blog_Post(author=account)
        serializer=Blog_PostSerializer(blog_post,data=blog_post)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"failed":"unable to create"}, status=status.HTTP_201_CREATED)

    def put(self,request,slug):
        serializer = Blog_PostSerializer(self.get_object(slug), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    def delete(self,request,slug):
        operation=self.get_object(slug).delete()
        if operation==True:
            return Response({"sucess":"delete sucessful"})
        return Response({"sucess":"delete failed"})


