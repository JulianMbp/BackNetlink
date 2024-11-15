# Generated by Django 5.1.1 on 2024-11-14 21:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0005_alter_experience_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinformation',
            name='abilities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='academicinformation',
            name='aditionalActivities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, size=None),
        ),
    ]