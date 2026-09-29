from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
