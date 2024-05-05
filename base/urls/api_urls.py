from django.urls import path, include
from rest_framework.routers import DefaultRouter

from base.api import category_views, file_views, folder_views, tags_views


router = DefaultRouter()
router.register(r'categories', category_views.CategoryViewSet)
router.register(r'files', file_views.FileViewSet)
router.register(r'folders', folder_views.FolderViewSet)
router.register(r'tags', tags_views.TagViewSet)

urlpatterns = [

    path('viewsets/', include(router.urls)),

    path('category/all', category_views.CategoryListApiView.as_view(), name='category_list_api'),
    path('category/<int:pk>', category_views.CategoryDetailApiView.as_view(), name='category_detail_api'),

    path('file/all', file_views.FileListApiView.as_view(), name='file_list_api'),
    path('file/<int:pk>', file_views.FileDetailApiView.as_view(), name='file_detail_api'),

    path('folder/all', folder_views.FolderListApiView.as_view(), name='folder_list_api'),
    path('folder/<int:pk>', folder_views.FolderDetailApiView.as_view(), name='folder_detail_api'),

    path('tag/all', tags_views.TagListApiView.as_view(), name='tag_list_api'),
    path('tag/<int:pk>', tags_views.TagDetailApiView.as_view(), name='tag_detail_api'),

]