# Generated by Django 4.2.8 on 2023-12-16 01:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Juegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('subnombre', models.CharField(max_length=30)),
                ('cuerpo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=30)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2023, 12, 15, 22, 30, 54, 358910))),
                ('imagen', models.ImageField(upload_to='Juegos')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=300)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2023, 12, 15, 22, 30, 54, 359992))),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Juegos.juegos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
