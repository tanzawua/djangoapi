# Generated by Django 4.1.2 on 2022-10-22 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiservicio', '0007_alter_servicio_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='nuevo',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='precio',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
