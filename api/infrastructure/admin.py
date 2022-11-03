from django.contrib import admin

from .models import *


@admin.register(Data)
class ImageAdmin(admin.ModelAdmin):
    list_display=('chrom', 'pos', 'alt', 'ref', "id_data")
