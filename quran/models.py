from django.db import models

# Create your models here.

class Reader(models.Model):
    name = models.CharField(max_length=250)
    name_ar = models.CharField(max_length=250)

    class Meta:
        ordering  = ('name',)

    def __str__(self):
        return self.name

class Recitations(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='recitations')
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=250)
    name_ar = models.CharField(max_length=250)
    read_surat_link = models.URLField()
    download_surat_link = models.URLField()
    surat_time = models.CharField(max_length=100)

    class Meta:
        ordering  = ('id',)

    def __str__(self):
        return self.name