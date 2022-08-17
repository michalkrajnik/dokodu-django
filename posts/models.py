from django.db import models


# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'/{self.id} {self.title}'
