from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
