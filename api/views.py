from rest_framework import viewsets
from .serializers import BookSerializer, VideoSerializer
from .models import Book,Video
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# class ImageViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def post(self, request, *args, **kwargs):
#         cover = request.data['cover']
#         title = request.data['title']
#         Book.objects.create(title=title, cover=cover)
#         return Response({'message': 'Book created'}, status=200)


class ImageViewSet(viewsets.ViewSet):
    def list(self,request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk= None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk= pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    # def update(self, request, pk = None):
    #
    #     book = BookSerializer.objects.get(pk= pk)
    #
    #     serializer = BookSerializer(book, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk= None):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class VideoViewSet(viewsets.ViewSet):
    def list(self, request):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk= None):
        queryset = Video.objects.all()
        video = get_object_or_404(queryset, pk= pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    # def update(self, request, pk = None):
    #     video = BookSerializer.objects.get(pk= pk)
    #
    #     serializer = VideoSerializer(video, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk= None):
        video = Video.objects.get(pk=pk)
        video.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


