from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrPublic


# Create your views here.

# User Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Post/Blog Viewset
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrPublic, permissions.IsAuthenticatedOrReadOnly]

# Like ViewSet
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]