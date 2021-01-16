from django.urls import path     
from . import views                   # imports the views file that is in the same app

urlpatterns = [
    path('', views.index),	   
]
