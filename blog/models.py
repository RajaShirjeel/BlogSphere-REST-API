from django.db import models
from django.conf import settings


class Post(models.Model):
    STATUSES = [("D", "Draft"), ("P", "Published")]
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    status = models.CharField(max_length=1, choices=STATUSES, default="D")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        ordering = ["-created_at"]
        permissions = [("feature_post", "Can feature a post")]
