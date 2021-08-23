from django.contrib import admin
from .models import Book, Video

# admin.site.register(Book)

@admin.register(Book)
class Image_Upload(admin.ModelAdmin):
    list_filter = ('title','cover')
    list_display = ('title','cover')


@admin.register(Video)
class Image_Upload(admin.ModelAdmin):
    list_filter = ('caption','title')
    list_display = ('caption','title')

