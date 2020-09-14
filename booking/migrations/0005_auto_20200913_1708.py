# Generated by Django 3.1 on 2020-09-13 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='location',
            new_name='location_id',
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='booking',
            name='location',
        ),
    ]
