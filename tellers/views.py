from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Index of teller application")