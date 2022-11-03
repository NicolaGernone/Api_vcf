# Generated by Django 4.1.3 on 2022-11-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_data_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='alt',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='chrom',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='data',
            name='filter',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='format',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.CharField(blank=True, max_length=1000, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='data',
            name='info',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='nas',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='qual',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='ref',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
