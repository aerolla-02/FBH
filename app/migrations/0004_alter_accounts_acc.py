# Generated by Django 5.1.7 on 2025-04-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_accounts_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='acc',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
