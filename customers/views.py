from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    message = "You are on index page of customer view"
    return render(request, 'customers/index.html', {'message':message})
