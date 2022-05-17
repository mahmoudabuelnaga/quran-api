from django.contrib import admin
from .models import Reader, Recitations
from import_export.admin import ImportExportModelAdmin
from django.shortcuts import render

# Register your models here.
admin.site.register(Reader)

@admin.register(Recitations)
class CharactersAdmin(ImportExportModelAdmin):
    pass
