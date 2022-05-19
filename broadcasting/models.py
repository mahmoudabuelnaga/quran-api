from django.db import models

# Create your models here.

class Broadcasting(models.Model):
    STATUS_TYPE = (
        ('reading', 'Reading'),
        ('science', 'Science and Interpretation'),
        ('translators', 'Translators'),
    )
    title_en = models.CharField(max_length=250)
    riwaya_en = models.CharField(max_length=250, null=True, blank=True)
    title_ar = models.CharField(max_length=250)
    riwaya_ar = models.CharField(max_length=250, null=True, blank=True)
    broadcasting = models.URLField()
    status_type = models.CharField(max_length=20, choices=STATUS_TYPE)

    class Meta:
        ordering = ('status_type', )

    def __str__(self):
        return self.title_en