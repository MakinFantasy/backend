from rest_framework import pagination

class FilePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class FolderPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class CategoryPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class TagPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
