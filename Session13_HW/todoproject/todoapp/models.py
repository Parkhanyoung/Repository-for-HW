from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date = models.DateTimeField()
    written_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=None)

    def __str__(self):
        return self.title


class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', default=None)

    def __str__(self):
        return self.content


class Like(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')


class Scrap(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='scraps')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scraps')