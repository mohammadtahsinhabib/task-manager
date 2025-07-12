from django.shortcuts import render,redirect,HttpResponse
from users.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import *
from users.forms import LoginForm,AssignmentForm,CreateGroupForm
from django.contrib import messages
from django.db.models import Prefetch 


# Create your views here.

def sign_up(request):
    form = RegistrationForm()
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.is_aactive = False
            user.save()

            messages.success(request,"A congirmation email sent to your email")
            return redirect('sign-in')

    return render(request, 'registration/sign_up.html',{"form":form})


def sign_in(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    return render(request, 'registration/sign_in.html', {'form': form})

@login_required
def sign_out(request):
    if request.method == 'POST':
        logout(request)
    
    return redirect('home')
    



def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('sign-in')
        else:
            return HttpResponse('Invalid Id or token')

    except User.DoesNotExist:
        return HttpResponse('User not found')

def is_admin(user,login_url ='no-permission'):
    return user.groups.filter(name='Admin').exits()

@user_passes_test(is_admin)
def admin_dashboard(request):
    users = User.objects.prefetch_related(Prefetch('groups', queryset=Group.objects.all(), to_attr='all_groups')).all()

    for user in users:
        if user.all_groups: user.group_name=user.all_groups[0].name
        else: user.group_name='No Permission'
    return render(request,'admin/dashboard.html',{"users" : users})

@user_passes_test(is_admin)
def assign_role(request, user_id):
    user = User.objects.get(id=user_id)
    form = AssignmentForm()

    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request, f"User {user.username} has been assigned to the {role.name} role")
            return redirect('admin-dashboard')
    return render(request, 'admin/assign_role.html', {"form": form})


def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'admin/group_list.html', {'groups': groups})



def create_group(request):
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)

        if form.is_valid():
            group = form.save()
            messages.success(request, f"Group {group.name} has been created successfully")
            return redirect('create-group')
        
    return render(request, 'admin/create_group.html', {'form': form})