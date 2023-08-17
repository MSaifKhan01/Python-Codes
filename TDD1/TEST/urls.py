
from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:city>/',views.weather,name='weather'),
    path('create',views.Create,name='create')
]