from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import os

from django.contrib.auth import get_user_model
User = get_user_model()

#class based views  with authhentation

from  rest_framework.views import APIView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser


class ArticalAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAdminUser]
    def get(self,request):
        # lst=[]
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        # for i in request.session:
        #    lst.append(i)
        # if 'username' in request.session:
        #     username=request.session["username"]
        # return Response(serializer.data)
        # return Response((request.session)["_auth_user_id"])
        return Response(str(User.objects.get(pk=(request.session)["_auth_user_id"])))

    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticalDetails(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self,id):
        try:
            article = Article.objects.get(id=id)
            return article
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request,pk):
            serializer = ArticleSerializer(self.get_object(pk))
            return Response(serializer.data)

    def put(self,request,pk):
        serializer = ArticleSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







#Method based views
@csrf_exempt

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method =='GET':
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    """
    Retrieve, update or delete a code article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)