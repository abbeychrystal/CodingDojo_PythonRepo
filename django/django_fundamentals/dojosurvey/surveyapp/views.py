from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'form.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'lang': request.POST['language'],
            'loc': request.POST['location'],
            'stoke': request.POST['stoke'],
        }
        return render(request, 'result.html', context)
    return render (request, 'result.html')