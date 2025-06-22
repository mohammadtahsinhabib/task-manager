from django.shortcuts import render
from django.http import HttpResponse


def manager_dashboard(request):
    return render(request,"admin_dashboard.html")

def user_dashboard(request):
    return render(request,"user_dashboard.html")
    
