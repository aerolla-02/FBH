# Generated by Django 5.1.7 on 2025-04-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_accounts_aadhar_alter_accounts_mobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='otp',
            field=models.IntegerField(default=0),
        ),
    ]
