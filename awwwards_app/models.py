from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    full_name = models.CharField(max_length = 50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')

    def __str__(self):
        return self.full_name


class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = CloudinaryField('image')
    description = models.TextField()
    live_link = models.URLField(max_length = 200)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'projects')

    def __str__(self):
        return self.title
