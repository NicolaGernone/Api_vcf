from django.db import models

class Data(models.Model):
    chrom = models.SlugField(max_length=100000)
    pos = models.IntegerField(default=0, editable=True)
    alt = models.SlugField(max_length=100000, null=True, blank=True)
    ref = models.SlugField(max_length=100000, null=True, blank=True)
    id_data = models.SlugField(max_length=100000, blank=True)
    qual = models.SlugField(max_length=100000, null=True, blank=True)
    filter = models.SlugField(max_length=100000, null=True, blank=True)
    info = models.SlugField(max_length=100000, null=True, blank=True)
    format = models.SlugField(max_length=100000, null=True, blank=True)
    nas = models.SlugField(max_length=100000, null=True, blank=True)

    class Meta:
        db_table = 'Data'
        verbose_name = "Data"
        verbose_name_plural = "Data"