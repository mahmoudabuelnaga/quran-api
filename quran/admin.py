from django.contrib import admin
from .models import Reader, Recitations
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Reader)

@admin.register(Recitations)
class RecitationsAdmin(ImportExportModelAdmin):
    pass
