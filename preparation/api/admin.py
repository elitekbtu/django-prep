from django.contrib import admin
from .models import Book, Author, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "uploaded_file", "updated_at", "created_at")
    search_fields = ("name", "description")
    list_filter = ("updated_at", "created_at")

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "photo", "updated_at", "created_at")
    search_fields = ("name", "surname")
    list_filter = ("updated_at", "created_at")

@admin.register
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "updated_at", "created_at")
    search_fields = ("name")
    list_filters = ("updated_at", "created_at")
