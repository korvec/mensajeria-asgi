from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.sala, name='sala'),
    path('global/', views.sala_global, name='sala_global'),
]
