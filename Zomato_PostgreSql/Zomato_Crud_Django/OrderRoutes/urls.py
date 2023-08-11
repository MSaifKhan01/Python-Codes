from django.urls import path
from . import views
urlpatterns = [
    path('get',views.GetOrder,name='get'),
    path('create',views.CreateOrder,name='create'),
    path('update/<int:itemid>',views.Update,name='update'),
    path('delete/<int:itemid>',views.Delete,name='delete')
]