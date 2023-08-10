from django.urls import path
from . import views
urlpatterns = [
    path('get',views.GetOrder,name='get'),
    path('create',views.CreateOrder,name='create'),
    path('update',views.Update,name='update'),
    path('delete',views.Delete,name='delete')
]