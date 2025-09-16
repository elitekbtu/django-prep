from django.db import models

# Create your models here
class Author(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=128)
    photo = models.FileField(upload_to="authors_avatars/")

    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=128)

    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to="books/")

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")

    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

