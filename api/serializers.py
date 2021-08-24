from rest_framework import serializers
from .models import Upload_Image_Video

class Upload_Image_Video_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Upload_Image_Video
        fields = ['id', 'title', 'date', 'caption', 'cover', 'type']

# class VideoSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Video
#         fields = ['id', 'caption', 'title', 'video']