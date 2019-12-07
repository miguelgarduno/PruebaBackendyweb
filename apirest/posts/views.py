# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer


class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()


class PostViewset(BaseViewSet):
    serializer_class = PostSerializer
    model = Post
