from django.db import models

# Create your models here.
from django.db import models

def upload_path(instance, filename):
    return '/'.join(['album', str(instance.title), filename])



class Upload_Image_Video(models.Model):

    choices = (('I', 'Image'),
              ('V', 'Video'))

    title = models.CharField(max_length=32, blank=False)
    date = models.DateTimeField()
    caption = models.CharField(max_length=256, blank=False)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)
    type = models.CharField(max_length=1, choices=choices, default='Image')

    def __str__(self):
        return self.title