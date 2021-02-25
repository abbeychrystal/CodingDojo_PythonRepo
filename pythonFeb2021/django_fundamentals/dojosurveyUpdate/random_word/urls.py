from django.urls import path
from . import views

urlpatterns = [
    path('', views.rand_word),
    path('reset', views.reset)

]
