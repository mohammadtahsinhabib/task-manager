from django.shortcuts import render,redirect
from users.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def sign_up(request):
    form = RegistrationForm()
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            User.objects.create_user(
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                password=user_data['password']
            )
            return render(request,'registration/sign_up_success.html')

    return render(request, 'registration/sign_up.html',{"form":form})


def sign_in(request):
    if request.method == 'POST':
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')
        user = authenticate(request, username=input_username, password=input_password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/sign_in.html')


def sign_out(request):
    if request.method == 'POST':
        logout(request)
    
    return redirect('home')
    