# Generated by Django 5.1.7 on 2025-04-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='Aadhar',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='mobile',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='pan',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
