# Generated by Django 4.2.8 on 2023-12-14 23:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0002_mensajes'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegos',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]