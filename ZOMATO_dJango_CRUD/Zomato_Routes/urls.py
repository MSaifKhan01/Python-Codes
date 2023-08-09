from django.urls import path
from . import views
urlpatterns = [
    path("",views.Get,name='get'),
    path("create",views.Create,name='create'),
    path("update",views.Update,name='update'),
    path("delete",views.Delete,name='delete'),
    path("order",views.Userorder,name='order'),
    path("view",views.orderGet,name='orderget'),
]