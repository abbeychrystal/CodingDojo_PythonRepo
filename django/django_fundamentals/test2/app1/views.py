from django.shortcuts import render     #, HttpResponse

# Create your views here.

# def index(request):                          #example of returning a string only to the rendered webpage, good for testing. Don't forget to import 'HttpResponse' along with 'render' from django.shortcuts in first lines on views.py
#     return HttpResponse("This is my response!")

# def index(request):                         #example of syntax for introducing first template
#     return render(request, "index.html")

def index(request):
    context = {
        "name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)