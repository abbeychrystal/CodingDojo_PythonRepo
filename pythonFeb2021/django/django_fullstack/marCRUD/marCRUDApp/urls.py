from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('chickens/create', views.create_chicken),
]