from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.post_list_view, name="post_list_view"),
    path("posts/<int:pk>/", views.post_detail_view, name="post_detail_view"),
]
