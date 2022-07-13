from django.contrib import admin
from .models import Reader, Recitations
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Reader)
class ReaderAdmin(ImportExportModelAdminm, admin.ModelAdmin):
    list_display = ['name_ar', 'name']
    search_fields = ['name_ar', 'name']
    list_editable = ['name_ar', 'name']


@admin.register(Recitations)
class RecitationsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['reader', 'number', 'name_ar', 'name','surat_time']
    list_filter = ['reader']
    search_fields = ['reader', 'number', 'name_ar']
    list_editable = ['number', 'name_ar', 'surat_time']
