from django.contrib import admin
from .models import Category, Container, Component
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title_ar', 'title', 'number']
    search_fields = ['title_ar', 'title','number']
    list_editable = ['number']

@admin.register(Container)
class ContainerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title_ar', 'title', 'number', 'category']
    list_filter = ['category']
    search_fields = ['title_ar', 'title','number']
    list_editable = ['number']

@admin.register(Component)
class ComponentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['container', 'number']
    list_filter = ['container']
    search_fields = ['body', 'surat','bismillah']
    list_editable = ['number',]
