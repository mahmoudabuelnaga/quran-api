from django.contrib import admin
from .models import Category, Container, Component
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Category)
class RecitationsAdmin(ImportExportModelAdmin):
    pass

@admin.register(Container)
class RecitationsAdmin(ImportExportModelAdmin):
    pass


@admin.register(Component)
class RecitationsAdmin(ImportExportModelAdmin):
    pass