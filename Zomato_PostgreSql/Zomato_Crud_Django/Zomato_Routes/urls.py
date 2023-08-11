from django.urls import path
from . import views
urlpatterns = [
    path('create',views.Create,name='create'),
    path('get',views.Get,name='get'),
    path('update/<int:itemid>',views.Update,name='update'),
    path('delete/<int:itemid>',views.Delete,name='delete')
  
]