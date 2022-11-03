from django.core.management.base import BaseCommand, CommandError
from api.application.domain.entity.vcf_entity import Data
from db.vcf_reader import read_vcf_data

class Command(BaseCommand):
    help = 'load all the vcf data in the Data Base'

    def add_arguments(self, parser):
        parser.add_argument('vcf_path', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            vcf_data, vcf_names = read_vcf_data(options['vcf_path'][0]) 
            for i in vcf_data:
                print(i)
        except IOError:
            raise CommandError('File does not exist')

        ##poll.opened = False
        ##poll.save()

        self.stdout.write(self.style.SUCCESS('Successfully closed'))