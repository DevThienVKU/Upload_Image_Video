from django.urls import path, include
from .views import Upload_Image_Video_Viewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('albums', Upload_Image_Video_Viewset, basename='albums')

# router.register('videos', VideoViewSet, basename='videos')


urlpatterns = [
    path('', include(router.urls)),

]