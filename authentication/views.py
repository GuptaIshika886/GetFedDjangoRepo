from django.shortcuts import render
from . models import RegisteredUsers
from .serializers import RegisteredUsersSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json
from .serializers import ResaurantsModelsSerializers
from . models import RestuarantsModels
# Create your views here.

@csrf_exempt
def usersDetail(request):
    many=True
    if request.method=='GET':
        regusers=RegisteredUsers.objects.all()
        serializer=RegisteredUsersSerializers(regusers,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method=='POST':
        jsonData=JSONParser().parse(request)
        serializer=RegisteredUsersSerializers(data=jsonData)
        # print(jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

def restaurantsDetails(request):
    if request.method=='GET':
        resDetails=RestuarantsModels.objects.all()
        serializer=ResaurantsModelsSerializers(resDetails,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
