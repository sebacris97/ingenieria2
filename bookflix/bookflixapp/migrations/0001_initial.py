# Generated by Django 3.0.6 on 2020-05-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('nropaginas', models.PositiveIntegerField()),
                ('nrocapitulos', models.PositiveIntegerField()),
                ('isbn', models.PositiveIntegerField()),
                ('autor', models.CharField(max_length=200)),
                ('editorial', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('agnoedicion', models.DateField()),
            ],
        ),
    ]