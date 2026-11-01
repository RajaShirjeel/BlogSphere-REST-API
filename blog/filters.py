from django_filters.rest_framework import FilterSet
from rest_framework.filters import OrderingFilter

from .models import Post


class PostOrderingFilter(OrderingFilter):
    def get_ordering(self, request, queryset, view):
        ordering = super().get_ordering(request, queryset, view)

        if not ordering:
            return ordering

        ordering = list(ordering)

        if not any(item.lstrip("-") in ("id", "pk") for item in ordering):
            ordering.append("id")

        return ordering


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {"created_at": ["gt", "lt"]}
