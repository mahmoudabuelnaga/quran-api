from django.contrib import admin
from .models import Reader, Recitations
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Reader)
class ReaderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'name_ar',]
    search_fields = ['name', 'name_ar',]
    # list_editable = ['name', 'name_ar',]


@admin.register(Recitations)
class RecitationsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'reader', 'number', 'name_ar', 'surat_time']
    list_filter = ['reader']
    search_fields = ['reader', 'number', 'name_ar']
    list_editable = ['number', 'name_ar', 'surat_time']
