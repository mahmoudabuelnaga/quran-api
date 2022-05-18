from operator import mod
from django.db import models

# Create your models here.

class AsmaAlHusna(models.Model):
    number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=250)
    transliteration = models.CharField(max_length=250)
    meaning = models.CharField(max_length=250)

    class Meta:
        ordering = ('number',)

    def __str__(self):
        return self.name