from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly, CanFeaturePost
from .filters import PostFilter, PostOrderingFilter


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status="P")
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, PostOrderingFilter]
    search_fields = ["title", "author__username", "content"]
    ordering_fields = ["title", "id", "created_at", "updated_at"]
    filterset_class = PostFilter

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
