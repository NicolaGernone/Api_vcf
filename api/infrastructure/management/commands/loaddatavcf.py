from db.populate_db import db_load
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'load all the vcf data in the Data Base'

    def add_arguments(self, parser):
        parser.add_argument('vcf_path', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            db_load(options['vcf_path'][0]) 
            self.stdout.write(self.style.SUCCESS('Successfully uploded'))
        except IOError:
            raise CommandError('File does not exist')

        self.stdout.write(self.style.SUCCESS('Successfully closed'))
            

        
