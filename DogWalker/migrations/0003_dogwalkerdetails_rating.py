# Generated by Django 4.1.7 on 2023-03-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DogWalker', '0002_rename_buyerpost_dogwalkerdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogwalkerdetails',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
