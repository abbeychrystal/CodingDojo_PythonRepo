from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if "amount" not in request.session:
        request.session["amount"] = 0
    if "activities" not in request.session:
        request.session["activities"] = []
    return render(request, "index.html")

def process_money(request):
    if request.method == "POST":
        if request.POST["place"] == "Farm":
            randomnum = random.randint(10,20)
            request.session["amount"] += randomnum  
            randomstr = f"Farm gained {randomnum} pieces of gold"
            request.session["activities"].append(randomstr)
        elif request.POST["place"] == "Cave":
            randomnum = random.randint(5,10)
            request.session["amount"] += randomnum  
            randomstr = f"Cave gained {randomnum} pieces of gold"
            request.session["activities"].append(randomstr)
        elif request.POST["place"] == "House":
            randomnum = random.randint(2,5)
            request.session["amount"] += randomnum  
            randomstr = f"House gained {randomnum} pieces of gold"
            request.session["activities"].append(randomstr)
        else:
            randomnum = random.randint(-50,50)
            request.session["amount"] += randomnum
            if randomnum >= 0:
                randomstr = f"Casino gained {randomnum} pieces of gold"
            else:
                randomstr = f"Casino lost {randomnum} pieces of gold"
            request.session["activities"].append(randomstr)
    return redirect("/")

def reset(request):
    if request.method == "POST":
        request.session.flush()
    return redirect("/")