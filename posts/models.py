from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'/{self.id} {self.title}'
