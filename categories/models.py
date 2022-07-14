from unicodedata import category
from django.db import models
from django.utils.text import slugify
from tinymce import models as tinymce_models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250)
    title_ar = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    number = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Categorios'
        ordering  = ('number',)

    def __str__(self):
        return self.title_ar
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Container(models.Model):
    title = models.CharField(max_length=250)
    title_ar = models.CharField(max_length=250)
    number = models.PositiveIntegerField()
    slug = models.SlugField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='containers')

    class Meta:
        ordering  = ('number',)

    def __str__(self):
        return self.title_ar
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Container, self).save(*args, **kwargs)



class Component(models.Model):
    number = models.PositiveIntegerField()
    container = models.ForeignKey(Container, on_delete=models.CASCADE, related_name='components')
    bismillah = models.CharField(max_length=50, null=True, blank=True)
    body = tinymce_models.HTMLField() # body = models.TextField()
    surat = models.CharField(max_length=50, null=True, blank=True)
    looper = models.PositiveIntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering  = ('number',)

    def __str__(self):
        return f"{self.container.title_ar} - {self.id}"
