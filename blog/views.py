from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly, CanFeaturePost


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsAuthenticatedOrReadOnly, CanFeaturePost],
    )
    def toggle_feature(self, request, pk):
        post = self.get_object()
        post.is_featured = not post.is_featured
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)
