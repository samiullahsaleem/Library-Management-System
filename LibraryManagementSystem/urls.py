
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("Library.urls")),
    path("users/", include("Users.urls")),
    path("admin/", admin.site.urls),

]

