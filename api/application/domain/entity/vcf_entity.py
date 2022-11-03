from django.db import models

class Data(models.Model):
    chrom = models.CharField(max_length=1000)
    pos = models.IntegerField(default=0, editable=True)
    alt = models.CharField(max_length=1000, null=True, blank=True)
    ref = models.CharField(max_length=1000, null=True, blank=True)
    id = models.CharField(primary_key=True, max_length=1000, blank=True)
    qual = models.CharField(max_length=1000, null=True, blank=True)
    filter = models.CharField(max_length=1000, null=True, blank=True)
    info = models.CharField(max_length=1000, null=True, blank=True)
    format = models.CharField(max_length=1000, null=True, blank=True)
    nas = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = 'Data'
        verbose_name = "Data"
        verbose_name_plural = "Data"