# Generated by Django 4.1.7 on 2023-03-21 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image/')),
                ('Age', models.IntegerField()),
                ('Profession', models.CharField(blank=True, max_length=300)),
                ('Availability', models.CharField(max_length=300)),
                ('adress', models.CharField(max_length=220)),
                ('mobile_no', models.IntegerField(default=True)),
                ('Name', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
