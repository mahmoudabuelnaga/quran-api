from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AsmaAlHusna

# Register your models here.

@admin.register(AsmaAlHusna)
class AsmaAlHusnasAdmin(ImportExportModelAdmin):
    pass
