from django.db import models

# Create your models here.

class MediaData(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    image = models.ImageField(upload_to='userimg/', blank=True,null=True)
    