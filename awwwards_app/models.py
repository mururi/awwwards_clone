from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    full_name = models.CharField(max_length = 50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile', null = True)

    def __str__(self):
        return self.full_name


class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = CloudinaryField('image')
    description = models.TextField()
    live_link = models.URLField(max_length = 200)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'projects', null = True)

    def __str__(self):
        return self.title

class Rate(models.Model):
    design = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    creativity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    project = models.ForeignKey(Project, on_delete = models.CASCADE, null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)