from django.db import models

# Create your models here

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to="books/")
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=128)
    photo = models.FileField(upload_to="authors_avatars/")
    updated_at = models.DataTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)