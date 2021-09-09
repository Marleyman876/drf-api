from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework import generics
from .models import Blog

# Create your views here.

class blogpostlist(generics.ListCreateAPIView):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer

class blogpostdetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer