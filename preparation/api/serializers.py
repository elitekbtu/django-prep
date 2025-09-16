from rest_framework import serializers
from .models import Book, Author, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "description", "author", "category", "uploaded_file", "updated_at", "created_at"]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "surname", "photo", "updated_at", "created_at"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "updated_at", "created_at"]
