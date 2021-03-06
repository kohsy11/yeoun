from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Community(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'community', default = "")
    img = models.TextField(default="")

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(Community, on_delete=models.CASCADE, related_name = 'comments')
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments', default = "")

class Option(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'option')
    option1 = models.TextField()
    option2 = models.TextField()

class Leggings(models.Model):
    id = models.PositiveIntegerField(primary_key = True)
    title = models.CharField(max_length = 200)
    price = models.PositiveIntegerField()
    img_src = models.TextField()
    provider = models.CharField(max_length = 200)
    link = models.TextField()
    feature = models.CharField(max_length = 200)
    color = models.CharField(max_length = 200)