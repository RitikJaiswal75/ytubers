# Generated by Django 3.2.3 on 2021-05-22 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_basedetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basedetail',
            old_name='photo',
            new_name='phone',
        ),
    ]
