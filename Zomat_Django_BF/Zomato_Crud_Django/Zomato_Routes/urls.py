from django.urls import path
from . import views
urlpatterns = [
    path('create',views.Create,name='create'),
    path('get',views.Get,name="get")
]