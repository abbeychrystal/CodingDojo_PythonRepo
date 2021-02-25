from django.urls import path
from . import views

urlpatterns = [
    path('surveyapp', views.index),
    path('surveyapp/survey', views.survey),
    path('surveyapp/result', views.result)
]