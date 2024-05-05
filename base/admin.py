from django.contrib import admin

from .models import File, Tag, Folder, Category

from import_export import resources
from import_export.admin import ExportMixin
from import_export.formats import base_formats

from simple_history.admin import SimpleHistoryAdmin

class FileResource(resources.ModelResource):
    class Meta:
        model = File


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag


class FolderResource(resources.ModelResource):
    class Meta:
        model = Folder


class AdminHistoryModel(SimpleHistoryAdmin, admin.ModelAdmin):
    pass


class FolderInLine(admin.TabularInline):
    model = File
    extra = 1

@admin.register(File)
class FileAdmin(ExportMixin, AdminHistoryModel):
    resource_class = FileResource
    list_display = (
        'id', 'file_name', 'description', 'created_at',
    )
    list_filter = (
        'created_at','tags', 'category'
    )
    search_fields = (
        'file_name__startswith',
        'description__startswith'
    )

    date_hierarchy = 'created_at'

    def get_export_formats(self):
        formats = [
            base_formats.XLSX,
            base_formats.CSV,
            base_formats.JSON
        ]

        return [format for format in formats if format().can_export()]



@admin.register(Category)
class CategoryAdmin(ExportMixin, AdminHistoryModel):

    resource_class = CategoryResource

    list_display = (
        'name', 'image', 'created_at'
    )

    list_filter = (
        'id', 'created_at'
    )

    search_fields = (
        'name__starswith',
    )

    filter_horizontal = (
        'files',
    )

    date_hierarchy = 'created_at'

    def get_export_formats(self):
        formats = [
            base_formats.XLSX,
            base_formats.CSV,
            base_formats.JSON
        ]

        return [format for format in formats if format().can_export()]


@admin.register(Tag)
class TagAdmin(ExportMixin, AdminHistoryModel):
    resource_class = TagResource

    list_display = (
        'name', 'created_at'
    )

    list_filter = (
        'created_at',
    )

    search_fields = (
        'name_startswith',
    )

    date_hierarchy = 'created_at'

    def get_export_formats(self):
        formats = [
            base_formats.XLSX,
            base_formats.CSV,
            base_formats.JSON
        ]

        return [format for format in formats if format().can_export()]
    

@admin.register(Folder)
class FolderAdmin(ExportMixin, AdminHistoryModel):
    inline = [FolderInLine]

    resource_class = FolderResource

    list_display = (
        'name', 'description', 'created_at'
    )

    list_filter = (
        'files', 'created_at'
    )

    search_fields = (
        'name__startswith',
        'description__startswith'
    )

    filter_horizontal = (
        'files',
    )

    date_hierarchy = 'created_at'

    def get_export_formats(self):
        formats = [
            base_formats.XLSX,
            base_formats.CSV,
            base_formats.JSON
        ]

        return [format for format in formats if format().can_export()]
