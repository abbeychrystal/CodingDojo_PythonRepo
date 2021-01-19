from django.shortcuts import render, redirect
LANGS = (
    'Python',
    'JavaScript',
    'C#',
    'Java'
)
LOCATIONS = (
    'San Jose',
    'Seattle',
    'Chicago',
    'Online'
)
STOKES = (
    'Low',
    'Medium',
    'High'
)

# Create your views here.

def index(request):
    context = {
        'locations': LOCATIONS,
        'languages': LANGS,
        'stokes': STOKES
    }
    return render(request, 'form.html',context)

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {    
        'name': request.POST['name'],
        'lang': request.POST['language'],
        'loc': request.POST['location'],
        'stoke': request.POST['stoke'],
        'comment':request.POST['comment']
    }
    return render(request, 'result.html', context)
    
def result(request):
    context = {
        'result': request.session['result']
    }    
    return render(request, 'result.html', context)