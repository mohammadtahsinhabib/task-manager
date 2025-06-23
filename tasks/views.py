from django.shortcuts import render
from django.http import HttpResponse


def manager_dashboard(request):
    return render(request,"dashboard/admin_dashboard.html")

def user_dashboard(request):
    return render(request,"dashboard/user_dashboard.html")
    
