import random
from django.db.utils import DataError
from .vcf_reader import read_vcf_data
from api.infrastructure.models import Data

def db_load(path):
    """Populate the DB with VCF records. Max 5000 records"""
    try:
        data, names = read_vcf_data(path)
        for i,d in enumerate(data):
            records, created = Data.objects.get_or_create(chrom=d[0],
                                                            pos=d[1],
                                                            id_data= d[2] if d[2] != '.' else "rs"+ random.randrange(100, 1000000),
                                                            ref=d[3],
                                                            alt=d[4],
                                                            qual=d[5],
                                                            filter=d[6],
                                                            format=d[7],
                                                            nas=d[8])
            if i > 5000:
                break
    except DataError as e:
        raise DataError(e)
