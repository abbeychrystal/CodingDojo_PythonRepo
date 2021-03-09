from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "all_chickens" : Chicken.objects.all()
    }
    return render(request, "index.html", context)

def create_chicken(request):
    if request.method == "POST":
        #create errors dictionary:
        errors = Chicken.objects.create_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect("/chickens/create")
        else:
            # if the errors object is empty, that means there were no errors! Proceed to create:
            chicken = Chicken.objects.create(name=request.POST["chicken_name"], color=request.POST["chicken_color"])
    return redirect("/")