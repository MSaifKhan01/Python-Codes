
from django.urls import path
from . import views


urlpatterns=[
    path("welcome/",views.Welcome,name="welcome"),
    path('hello/<str:name>',views.Hello,name="Hello"),
    path('farewell/<str:greet>',views.Farewell,name="farewell")
]
