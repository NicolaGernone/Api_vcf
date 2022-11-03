from vcf_reader import read_vcf_data
from api.infrastructure.models import Data

def db_load(path):
    vcf_data, vcf_names = read_vcf_data(options['vcf_path'][0]) 
    for i in vcf_data:
        Data.object.create()