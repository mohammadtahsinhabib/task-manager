from django.db import models

# Create your models here.

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    position = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Task(models.Model):
    
    project = models.ForeignKey("Project",on_delete=models.CASCADE,default=1)
    employees=models.ManyToManyField(Employee)

    title = models.CharField(max_length=250)
    description = models.TextField()
    due_data=models.DateField()
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class TaskDetails(models.Model):
    HIGH,MEDIUM,LOW="H","M","L"
    PRIORITY_OPTIONS=(
        (HIGH, "High"),
        (MEDIUM,"Medium"),
        (LOW,"Low"),
    )
    
    Task=models.OneToOneField(Task,on_delete=models.CASCADE)
    assigned_to=models.CharField(max_length=250)
    priority=models.CharField(max_length=1,choices=PRIORITY_OPTIONS,default=LOW,)

class Project(models.Model):
    name =models.CharField(max_length=250)
    start_date = models.DateField()

