from django.conf.urls import url
from . import views
from django.urls import path

appname = 'services'

urlpatterns = [
    path('', views.Home),
    path('maps/', views.maps, name='maps'),
]
