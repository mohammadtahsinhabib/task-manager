from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("welcome to Home")

def contact(request):
    return HttpResponse("welcome to Contact")

def show_task(request):
    return HttpResponse("welcome to Show Task")
    
