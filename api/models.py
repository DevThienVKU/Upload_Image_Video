from django.db import models

# Create your models here.
from django.db import models

def upload_path(instance, filename):
    return '/'.join(['image', str(instance.title), filename])

def upload_video_path(instance, filename):
    return '/'.join(['video', str(instance.title), filename])

class Book(models.Model):
    title = models.CharField(max_length=32, blank=False)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)

class Video(models.Model):
    caption = models.CharField(max_length=100)
    title = models.CharField(max_length=32, blank=False)
    video = models.FileField(blank=True, null=True, upload_to=upload_video_path)

    def __str__(self):
        return self.caption