from typing import List
import pandas as pd
import gzip

def read_vcf_data(vcf_path) -> List:
    """Vcf reader"""
    with gzip.open(vcf_path, "rt") as ifile:
        for line in ifile:
            if line.startswith("#CHROM"):
                vcf_names = [x for x in line.split('\t')]
                break
        vcf = pd.read_csv(vcf_path, on_bad_lines='skip', compression='gzip', comment='#', chunksize=10000, delim_whitespace=True, header=None, names=vcf_names)
    return vcf.read().values, vcf_names


    

