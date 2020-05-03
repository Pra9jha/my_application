from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth import get_user_model
# User = get_user_model()
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from .log import print_log
from passlib.hash import pbkdf2_sha256
# def enc_pswd(user_data):
    # password=user_data['password']
    # enc_pass=pbkdf2_sha256.encrypt(password,rounds=1200,salt_size=32)
    # user_data['password']=enc_pass
    # return user_data
    # print_log(user_data)
    # print_log(pbkdf2_sha256.verify(password,enc_pass))
    # user_data.set_password(password)


from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser


class UserApi(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self,request):
        u_id = request.session["_auth_user_id"]
        print_log(request.session)
        user = User.objects.get(id=u_id)
        # print_log("{}  {}".format(u_id,user))
        return user
    def get(self,request):
        print_log("into get ")
        serializer = UserSerializer(self.get_object(request))
        print_log(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        # request_data=enc_pswd(request.data)
        # print_log(request_data)
        # serializer = UserSerializer(data=request_data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user_data=request.data
        print_log(user_data)
        user= User(email=user_data['email'],name=user_data['name'],is_active=user_data['is_active'],is_staff=user_data['is_staff'])
        user.set_password(user_data['password'])
        user_data['password']=user.password
        print_log(user_data)
        serializer = UserSerializer(data=user_data)
        print_log(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



