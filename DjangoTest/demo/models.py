from django.db import models
import django.utils.timezone as timezone

class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['id']

class MyModel(models.Model):
    string1 = models.CharField(max_length=10)
    string2 = models.CharField(max_length=10)
    create_time = models.DateTimeField(default = timezone.now)
    edit_time = models.DateTimeField(auto_now = True)
    result = models.TextField(null=True)