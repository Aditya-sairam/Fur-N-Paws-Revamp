from django.db import models
from django.contrib.auth.models import User
from blog.models import ITEM_CHOICES


# Create your models here.


class DogWalkerDetails(models.Model):
    Name = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='media/image/', blank=True, null=True)
    Age = models.IntegerField()
    Profession = models.CharField(max_length=300,blank=True)
    Availability = models.CharField(max_length=300)
    adress = models.CharField(max_length=220)
    mobile_no = models.IntegerField(default=True)