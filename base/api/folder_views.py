from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from base.models import Folder
from base.pagination import FolderPagination
from base.serializers import FolderSerializer

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    pagination_class = FolderPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['id']


class FolderListApiView(APIView, PageNumberPagination):
    def get(self, request, *args, **kwargs):
        folders = self.paginate_queryset(Folder.objects.all(), request, view=self)
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request, *args, **kwargs):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FolderDetailApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            folder = Folder.objects.get(pk=pk)
            serializer = FolderSerializer(folder)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Folder.DoesNotExist: 
            return Response(
                {
                    'error': 'Folder not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk, *args, **kwargs):
        try:
            folder = Folder.objects.get(pk=pk)
            serializer = FolderSerializer(folder, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        except Folder.DoesNotExist:
            return Response(
                {
                    'error': 'Folder not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, pk, *args, **kwargs):
        try:
            folder = Folder.objects.get(pk=pk)
            serializer = FolderSerializer(folder, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Folder.DoesNotExist:
            return Response(
                {
                    'error': 'Folder not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
                

    def delete(self, request, pk, *args, **kwargs):
        try:
            folder = Folder.objects.get(pk=pk)
            folder.delete()
            return Response(
                {
                    'status': 'success'
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except Folder.DoesNotExist:
            return Response(
                {
                    'error': 'Folder not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )