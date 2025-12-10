from django.contrib import admin
from main.models import Author, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_year', 'price', 'is_active', 'created_at')
    search_fields = ('title', 'genre')
    list_filter = ('is_active', 'published_year')
    ordering = ('-created_at',)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active', 'birth_date')