from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.
def home (request):
    #return HttpResponse('<h1>Welcome to Home Page </h1>')
    #return render(request, 'home.html')
    #return render(request, 'home.html', {'name':'Valeria Guerra'})
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm':searchTerm})

def about (request):
    return render(request, 'about.html')