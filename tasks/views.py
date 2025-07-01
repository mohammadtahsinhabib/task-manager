from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskModelForm,TaskForm
from tasks.models import Employee,Task


def manager_dashboard(request):
    return render(request,"dashboard/admin_dashboard.html")

def user_dashboard(request):
    return render(request,"dashboard/user_dashboard.html")

def create_task(request):
    employees=Employee.objects.all()
    forms=TaskModelForm()

    if request.method=="POST":
        forms=TaskModelForm(request.POST)

        if(forms.is_valid()):
            forms.save()
            return render(request,"task_form.html",{"forms":forms,"message" : "Submitted successfully"})
            # data = forms.cleaned_data()
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')

            # task = Task.objects.create(title=title, description=description, due_date=due_date)

            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employee)


            # return HttpResponse("Task Added successfully")

    context={"forms":forms}
    return render(request,"task_form.html",context)
    
