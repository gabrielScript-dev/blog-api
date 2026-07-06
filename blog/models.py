from django.db import models
from accounts.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title
