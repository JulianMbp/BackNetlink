# Generated by Django 5.1.1 on 2024-11-14 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_publicacion', '0003_publicacion_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='multimedia',
            field=models.ImageField(upload_to='publicaciones/'),
        ),
    ]
