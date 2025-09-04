from rest_framework import serializers
from .models import Book 


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "description", "uploaded_file", "updated_at", "created_at"]