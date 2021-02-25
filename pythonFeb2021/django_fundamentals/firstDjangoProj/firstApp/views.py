from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # return HttpResponse("This is my response!")
    return HttpResponse("Placeholder to display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog!")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}")

def destroy(request, number):
    return redirect('/')


#     A couple of important things to notice here:

# Every function's first argument will be the request object.
# We don't distinguish in our routes anywhere between GET vs POST requests. This will be done within a given function.
# If we are returning a string, we cannot simply return a string, but must send the string via HttpResponse (which must be imported. We'll be returning templates again soon enough!)