from django.urls import path
from . import views

urlpatterns = [
    path('addnewbook/', views.addNewBook, name='addnewbook'),
    path('search/', views.searchBook, name='search'),
    path('edit/<int:pk>/', views.editBook, name='edit'),
    path('delete/<int:pk>/', views.deleteBook, name='delete'),
]