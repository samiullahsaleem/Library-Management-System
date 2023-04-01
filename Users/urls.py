from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("loginform/", views.loginform, name="loginform"),
    path("logoutform/", views.logoutform, name="logoutform"),
    path("register/", views.register, name="register"),
    # path("profile/edit/", views.edit_profile, name="edit_profile"),
]