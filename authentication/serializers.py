from rest_framework import serializers
from .models import RegisteredUsers
from .models import RestuarantsModels

class RegisteredUsersSerializers(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    pwd=serializers.CharField(max_length=100)
    cpwd=serializers.CharField(max_length=100)

    def create(self,validate_data):
        print("Create Method Called")
        return RegisteredUsers.objects.create(**validate_data)

class ResaurantsModelsSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    phoneNo=serializers.CharField(max_length=12)
    possibleValues=serializers.CharField(max_length=500)
    # items=serializers.CharField(max_length=100)

    def create(self,validate_data):
        return RestuarantsModels.objects.create(**validate_data)