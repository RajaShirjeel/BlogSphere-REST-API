from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from . import models


class PostSerializer(ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Post
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "updated_at",
            "author",
            "slug",
            "status",
            "is_featured",
        ]
