from django.contrib import admin
from .models import RegisteredUsers
from .models import RestuarantsModels
# Register your models here.
@admin.register(RegisteredUsers)
class RegisteredUsersAdmin(admin.ModelAdmin):
    list_display=['id','username','email','pwd','cpwd']

@admin.register(RestuarantsModels)
class RestaurantsModelsAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phoneNo','possibleValues']