from django.db.utils import DataError
from .vcf_reader import read_vcf_data
from api.infrastructure.models import Data

def db_load(path):
    try:
        data, names = read_vcf_data(path)
        for d in data:
            records, created = Data.objects.get_or_create(chrom=d[0],
                                                            pos=d[1],
                                                            id_data=d[2],
                                                            ref=d[3],
                                                            alt=d[4],
                                                            qual=d[5],
                                                            filter=d[6],
                                                            format=d[7],
                                                            nas=d[8])
    except DataError as e:
        raise DataError(e)
