from .models import Blog_Post
from rest_framework import serializers

class Blog_PostSerializer(serializers.ModelSerializer):
        class Meta:
            model = Blog_Post
            fields = ['title' ,'body','image' ,'date_publish' ,'date_updated' ,'author']



