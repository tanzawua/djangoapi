# Generated by Django 4.1.2 on 2022-10-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiservicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(null=True, upload_to='Servicios'),
        ),
    ]
