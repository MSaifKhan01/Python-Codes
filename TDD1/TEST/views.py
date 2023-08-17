from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
# Create your views here.

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

def weather(req,city):
    if city in weather_data:
        return JsonResponse({"data":weather_data[city]})
    else:
        return JsonResponse({'data':'city not found'},status=404)
    

    
def Create(req):
    if req.method=="POST":
        body=json.loads(req.body)
        city=body.get('city')
        temperature=body.get('temperature')
        weather=body.get('weather')
        if city in weather_data:
            return JsonResponse({"data":"City already present"},status=401)
        else:
            weather_data[city]={"temperature":temperature,"weather":weather}
            return JsonResponse({"data":"data posted succesfully"})
    else:
        return JsonResponse({"data":"some error"},status=401)