from django.urls import path
from . import views
urlpatterns = [
    path('getorder',views.GetOrder,name='get'),
    path('createorder',views.CreateOrder,name='create'),
    path('updateorder/<int:itemid>',views.UpdateOrder,name='update'),
    path('deleteorder/<int:itemid>',views.DeleteOrder,name='delete')
]