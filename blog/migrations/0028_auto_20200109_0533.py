# Generated by Django 2.1.7 on 2020-01-09 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20200109_0450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='unique_name',
            new_name='slug',
        ),
    ]