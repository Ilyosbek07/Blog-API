from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly
from posts.serializers import PostSerializer, UserSerializer


# class PostListAPIView(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     permission_classes = (IsAuthorOrReadOnly,)
#
#
# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
