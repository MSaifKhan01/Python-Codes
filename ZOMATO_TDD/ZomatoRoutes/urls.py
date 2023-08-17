from django.urls import path
from . import views
urlpatterns = [
    path('createmenu',views.CreateMenu,name='create'),
    path('getmenu',views.GetMenu,name="get"),
    path('updatemenu/<int:itemid>',views.UpdateMenu,name='update'),
    path('deletemenu/<int:itemid>',views.DeleteMenu,name='delete')
]