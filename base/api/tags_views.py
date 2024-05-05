from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from base.models import Tag
from base.pagination import TagPagination
from base.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id']


class TagListApiView(APIView):
    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TagDetailApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tag.DoesNotExist:
            return Response(
                {
                    'error': 'Tag not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk, *args, **kwargs):
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        except Tag.DoesNotExist:
            return Response(
                {
                    'error': 'Tag not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, pk, *args, **kwargs):
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        except Tag.DoesNotExist:
            return Response(
                {
                    'error': 'Tag not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk, *args, **kwargs):
        try:
            tag = Tag.objects.get(pk=pk)
            tag.delete()
            return Response(
                {
                    'success': True
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except Tag.DoesNotExist:
            return Response(
                {
                    'error': 'Tag not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
