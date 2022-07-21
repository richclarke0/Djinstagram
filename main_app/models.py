from django.db import models

# Create your models here.
class Post:
    img = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    #continue here
    