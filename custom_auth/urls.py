from django.urls import path

from . import views

urlpatterns = [
    path("register/", view=views.RegisterView.as_view(), name="register"),
    path("login/", view=views.LoginView.as_view(), name="login"),
    path("logout/", view=views.LogoutView.as_view(), name="logout"),
    path("me/", view=views.UserView.as_view(), name="user"),
]
