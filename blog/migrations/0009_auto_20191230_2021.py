# Generated by Django 2.1.7 on 2019-12-30 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191230_2013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-published_date', '-updated', '-timestamp']},
        ),
    ]
