from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("You are on the index page of the bank")
