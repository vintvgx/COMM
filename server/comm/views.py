from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Tag, BlogPost, Comment, Like, Follow, Topic
from .serializers import UserSerializer, TagSerializer, TopicSerializer, BlogPostSerializer, CommentSerializer, LikeSerializer, FollowSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_serializer_context(self):
        # Pass the request object to the serializer context
        return {'request': self.request}

    @action(detail=False, methods=['get'])
    def user_posts(self, request, *args, **kwargs):
        # Retrieve and return the user's blog posts
        user = self.request.user
        posts = BlogPost.objects.filter(user=user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # Associate the current user with the 'user' field during creation
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

