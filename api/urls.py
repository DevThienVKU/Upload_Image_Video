from django.urls import path, include
from .views import ImageViewSet, VideoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('images', ImageViewSet, basename='images')
router.register('videos', VideoViewSet, basename='videos')


urlpatterns = [
    path('', include(router.urls)),

]