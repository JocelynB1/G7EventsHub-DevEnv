# Generated by Django 3.1 on 2020-09-13 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20200912_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='name',
            new_name='description',
        ),
    ]
