# Generated by Django 3.0.4 on 2020-05-16 07:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookflixapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='capitulo',
            options={'ordering': ['-numero'], 'verbose_name_plural': 'Capitulos'},
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='nropaginas',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Numero de paginas'),
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='numero',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Numero del capitulo'),
        ),
    ]
