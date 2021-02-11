# Michaels's solution:

from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('reset', views.reset),
    path('place/<str:place>', views.process),
]







# From platform solution: 
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index),
#     path('reset', views.reset),
#     path('gold', views.process_gold)
# ]


# My first attempt: 
# from django.urls import path
# from . import views
	
# urlpatterns = [
# 	    path('', views.index),
# 		path('gold', views.process_gold)
# 	]
