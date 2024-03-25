# Generated by Django 5.0.3 on 2024-03-25 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('address', models.CharField(max_length=200)),
                ('policies', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('doors_open', models.TimeField()),
                ('image', models.URLField()),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tick_it.venue')),
            ],
        ),
    ]
