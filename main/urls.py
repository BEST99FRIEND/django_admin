from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('books/', views.books_list, name='books_list'),
    path('authors/', views.authors_list, name='authors_list'),
]
