from rest_framework import serializers
from . models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email','name','is_active','is_staff','password']








