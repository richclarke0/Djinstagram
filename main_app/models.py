from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=175)
    email = models.CharField(max_length=175)
    profile_pic = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse(kwargs={'user_id': self.id})


class Post(models.Model):
    photo_url = models.URLField(max_length=200)
    description = models.TextField(max_length=250)
    # comments = ArrayField(
    #     models.CharField(max_length=512))
    favorite = ArrayField(
        models.CharField(max_length=512))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'post_id': self.id})
