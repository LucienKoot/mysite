from django.urls import path

from . import vieuws

urlpatterns = [
    path('', vieuws.index, name='index'),
]