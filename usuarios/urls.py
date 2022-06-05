from django.urls import path
from usuarios import views

urlpatterns = [
    path("api/user/", views.UserApi.as_view()),
    path("api/logout/", views.LogoutView.as_view(), name="auth_logout"),
]
