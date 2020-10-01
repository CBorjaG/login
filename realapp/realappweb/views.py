from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, "realappweb/home.html")

def galeria(request):
    return render(request, 'realappweb/galeria.html')