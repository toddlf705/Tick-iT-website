# Generated by Django 5.0.3 on 2024-03-25 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tick_it', '0002_remove_event_doors_open'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='address',
        ),
    ]