from django.db import models

class Data(models.Model):
    chrom = models.CharField(max_length=100)
    pos = models.IntegerField(default=0, editable=True)
    alt = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, unique=True, null=False, editable=True)

    class Meta:
        db_table = 'Data'
        verbose_name = "Data"
        verbose_name_plural = "Data"