from django.urls import path
from . import views # the . indicated that the views file can be found in the same directory as this file

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:number>', views.show),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy),
]
# This is the same url function as we saw in the project level urls.py, but this time our arguments indicate that:

# '' - the rest of the route both starts and ends with nothing (i.e. "/" is the full route), and
# views.index - if the requested route matches this pattern, then the function with the name "index" from this app's views.py file will be invoked.
# If the route wants a views.index function, then we'd better have one: ---> go to the app views.py file