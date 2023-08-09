from django.urls import path
from . import views

urlpatterns = [
    path('',views.Post,name='post'),
    path('get',views.Get,name='get'),
    path('update',views.Update,name='update'),
    path('delete',views.Delete,name='delete')
]