
from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.URLField(max_length=200)

    def __str__(self):
        return self.user.name

    # def get_absolute_url(self):
    #     return reverse(kwargs={'user_id': self.id})


class Post(models.Model):
    photo_url = models.URLField(max_length=200)
    caption = models.TextField(max_length=250)
    # comments = ArrayField(
    #     models.CharField(max_length=512))
    # favorite = ArrayField(
    #     models.CharField(max_length=512))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.caption

