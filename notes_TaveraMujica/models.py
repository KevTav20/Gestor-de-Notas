# Create your models here.
from tkinter.constants import CASCADE

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Note(models.Model):
    user =models.ForeignKey(User, on_delete = models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title