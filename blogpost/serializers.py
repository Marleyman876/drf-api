from django.db.models.base import Model
from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
      fields = ('id', 'author', 'title', 'body', 'created_at')
      model = Blog