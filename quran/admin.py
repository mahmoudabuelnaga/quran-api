from django.contrib import admin
from .models import Reader, Recitations
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Reader)
class RecitationsAdmin(ImportExportModelAdmin):
    pass

@admin.register(Recitations)
class RecitationsAdmin(ImportExportModelAdmin):
    pass