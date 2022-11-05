from api.infrastructure.models import Data
from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ['chrom', 'pos', 'id', 'ref', 'alt', 'qual', 'filter', 'info', 'format', 'nas']