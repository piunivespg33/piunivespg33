from django.urls import path
from usuarios import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.users, name="users"),
    path("cadastrarUsuario/", views.cadastrarUsuario, name="cadastrarUsuario"),
    path("logout/", views.user_logout, name="user_logout"),
    path("api/user/", views.UserApi.as_view()),
    path("api/logout/", views.LogoutView.as_view(), name="auth_logout"),
]
