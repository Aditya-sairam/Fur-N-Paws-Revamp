# Generated by Django 2.1.7 on 2020-01-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/image/default', upload_to='media/image/'),
        ),
    ]