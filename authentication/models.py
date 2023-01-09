from django.db import models

# Create your models here.

class RegisteredUsers(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    pwd=models.CharField(max_length=100)
    cpwd=models.CharField(max_length=100)

class RestuarantsModels(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phoneNo=models.CharField(max_length=12)
    possibleValues=models.CharField(max_length=500)
    # items=models.CharField(max_length=100)
    # availableItems=models.Lis

# class RestaurantModelValue(models.Model):
#     res_modesl=models.ForeignKey(RestuarantsModels,related_name='possibleValues')
#     value=models.TextField()


