from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from .serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
