from django.db import models
from django.contrib.auth.models import User

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

   
