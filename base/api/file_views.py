from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.reverse import reverse, reverse_lazy

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from base.models import File, Tag
from base.pagination import FilePagination
from base.serializers import FileSerializer

from datetime import date


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = FilePagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['file_name', 'description']
    filterset_fields = ['file_type', 'tags']
    ordering_fields = ['id']

    @action(detail=False, methods=['PATCH'])
    def remove_tag(self, request, *args, **kwargs):
        files = File.objects.all()
        tag = Tag.objects.get(pk=request.query_params['tag_id'])
        for file in files:
            if tag in file.tags.all():
                file.tags.remove(tag)
                file.save()
        return Response({'success': True}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def date_filter_month(self, request, *args, **kwargs):
        month = request.query_params.get('month', None)
        if month:
            queryset = File.objects.filter(
                Q(created_at__month=month)
            )
            serializer = FileSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'success': 'Вы не указали месяц'}, status=status.HTTP_404_NOT_FOUND)




    @action(detail=False, methods=['GET'])
    def date_filter_day_month(self, request, *args, **kwargs):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        month = request.query_params.get('month', None)
        if (not start) | (not month) | (not end):
            return Response({'succes': 'Не правильно указана дата'}, status=status.HTTP_404_NOT_FOUND)

        queryset = File.objects.filter(
            ~Q(created_at__day__lt=start) & ~Q(created_at__day__gt=end) & Q(created_at__month=month)
        )
        return Response(FileSerializer(queryset, many=True).data, status=status.HTTP_200_OK)

class FileListApiView(APIView, PageNumberPagination):
    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        data = self.paginate_queryset(files, request, view=self)
        serializer = FileSerializer(data, many=True, context={'request': request})

        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDetailApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            file = File.objects.get(pk=pk)
            serializer = FileSerializer(file)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except File.DoesNotExist:
            return Response(
                {
                    'error': 'File not found'
                },
                status = status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk, *args, **kwargs):
        try:
            file = File.objects.get(pk=pk)
            serializer = FileSerializer(file, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except File.DoesNotExist:
            return Response(
                {
                    'error': 'File not found'
                },
                status = status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, pk, *args, **kwargs):
        try:
            file = File.objects.get(pk=pk)
            serializer = FileSerializer(file, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except File.DoesNotExist:
            return Response(
                {
                    'error': 'File not found'
                },
                status = status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk, *args, **kwargs):
        try:
            file = File.objects.get(pk=pk)
            file.delete()
            return Response(
                {
                    'success': True
                },
                status = status.HTTP_200_OK
            )
        except File.DoesNotExist:
            return Response(
                {
                    'error': 'File not found'
                },
                status = status.HTTP_200_OK
            )