# Generated by Django 3.0.2 on 2020-12-30 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_recip'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recip',
            new_name='Recipe',
        ),
    ]
