from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "uploaded_file", "updated_at", "created_at")
    search_fields = ("name", "description")
    list_filter = ("updated_at", "created_at")

