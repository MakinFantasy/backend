from django.contrib import admin
from .models import File_tb, File, FileType



class File_tbAdmin(admin.ModelAdmin):
    list_display = ("file_name",
                    "description", "create_at", "file_type", "user_id")
    list_filter = ('file_type', "user_id",)
    search_fields = ("file_name__startswith",)


admin.site.register(File_tb, File_tbAdmin)


class FileAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 'name', 'create_at',
    )
    list_filter = ('create_at', 'user_id',)
    search_fields = ("file_name__startswith",)


admin.site.register(File, FileAdmin)


class FileTypeAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'filetype')
    list_filter = ('create_at', )
    search_fields = ("file_name__startswith",)


admin.site.register(FileType, FileTypeAdmin)
