from django.contrib import admin
from .models import Upload_Image_Video

# admin.site.register(Book)

@admin.register(Upload_Image_Video)
class Image_Upload(admin.ModelAdmin):
    list_filter = ('title', 'date', 'type')
    list_display = ('title', 'date', 'caption', 'cover', 'type')

#
# @admin.register(Video)
# class Image_Upload(admin.ModelAdmin):
#     list_filter = ('caption','title')
#     list_display = ('caption','title')

