from django.db import models
from cloudinary.models import CloudinaryField
from django.forms import CharField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = CloudinaryField('image')
    description = models.TextField()
    live_link = models.URLField(max_length = 200)
