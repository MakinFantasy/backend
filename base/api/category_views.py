from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import viewsets, status

from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from rest_framework.response import Response

from base.models import Category, File
from base.pagination import CategoryPagination
from base.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id']

    @action(methods=['DELETE'], detail=True)
    def delete_all_files(self, request, pk, *args, **kwargs):
        category = Category.objects.get(id=pk)
        category.files.clear()
        serializer = self.get_serializer(category)

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class CategoryListApiView(APIView, PageNumberPagination):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        data = self.paginate_queryset(categories, request, view=self)
        serializer = CategorySerializer(categories, many=True, context={'request': request})

        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response(
                {
                    'error': 'Category not found'
                },
                status = status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response(
                {
                    'error': 'Category not found'
                },
                status = status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response(
                {
                    'error': 'Category not found'
                },
                status = status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response(
                {
                    'success': True
                },
                status = status.HTTP_200_OK
            )
        except Category.DoesNotExist:
            return Response(
                {
                    'error': 'Category not found'
                },
                status = status.HTTP_200_OK
            )
