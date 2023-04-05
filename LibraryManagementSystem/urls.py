
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("users/", include("Users.urls")),
    path("library/", include("Library.urls")),
    path("admin/", admin.site.urls),

]

