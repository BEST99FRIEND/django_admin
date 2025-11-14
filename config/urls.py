
from django.contrib import admin
from django.urls import path
from main.views import hello, books_list, authors_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('books/', books_list, name='books_list'),
    path('authors/', authors_list, name='authors_list'),
]
