from django.shortcuts import render, redirect
from .models import Cow

# Create your views here.
def index(request):
    context = {
        "all_the_cows" = Cow.objects.all()    
    }
    return render(request, "index.html")

def create_cow(request):
    #create and instance
    cow = Cow.objects.create(name=request.POST['cow_name'], num_blades_grass= request.POST["grass"]. fav_activity=request.POST['activity'])
    # other attributes here
    #redirect
    return redirect('/')