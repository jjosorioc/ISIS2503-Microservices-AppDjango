
from .models import Place
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json



def PlacesList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)



def PlaceCreate(request):
    if request.method == 'POST':
        try:
            
            data = request.body.decode('utf-8')
            data_json = json.loads(data)
            place = Place()
            place.name = data_json['name']
            place.save()
            return HttpResponse("Successfully created a Place")
        except:
            return HttpResponse("Unsuccessfully created a measurement.")




def PlacesCreate(request):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            data_json = json.loads(data)
            places_list = []
            
            for place in data_json:
                db_place = Place()
                db_place.name = place['name']
                places_list.append(db_place)

            Place.objects.bulk_create(places_list)
            return HttpResponse('Successfully created Places')
        except:
            return HttpResponse('Unsuccesfully created Places')
