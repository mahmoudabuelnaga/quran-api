from django.contrib import admin
from .models import Broadcasting
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Broadcasting)
class BroadcastingAdmin(ImportExportModelAdmin):
    pass