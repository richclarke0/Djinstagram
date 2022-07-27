
from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)    
    profile_picture = models.URLField(max_length=200)

    def __str__(self):
        return self.user.username + " Profile"
        
            
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
    photo_url = models.URLField(max_length=200)
    caption = models.TextField(max_length=250)
    # comments = ArrayField(
    #     models.CharField(max_length=512))
    # favorite = ArrayField(
    #     models.CharField(max_length=512))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    date = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User, blank=None, related_name='likes')
 
    def __str__(self):
        return self.caption
    
    def num_likes(self):
        return self.liked.all().count()
    
  




    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.id})

class Comment(models.Model):
    body = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  f"{self.user}-{self.post}-{self.value}"