# Generated by Django 5.0.3 on 2024-03-25 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tick_it', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='doors_open',
        ),
    ]
