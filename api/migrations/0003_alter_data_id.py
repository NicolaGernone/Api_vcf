# Generated by Django 4.1.3 on 2022-11-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_data_filter_data_format_data_info_data_nas_data_qual_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.CharField(blank=True, max_length=100, primary_key=True, serialize=False),
        ),
    ]
