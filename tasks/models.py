from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES=[
        ("PENDING","Pending"),
        ("IN_PROGRESS","In Progress"),
        ("COMPLETED","Completed")
    ]

    project = models.ForeignKey("Project",on_delete=models.CASCADE,default=1)
    assigned_to = models.ManyToManyField(User,related_name="tasks")

    title = models.CharField(max_length=250)
    descriptions = models.TextField()
    due_date=models.DateField()
    status=models.CharField(max_length=15,choices=STATUS_CHOICES,default="PENDING")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class TaskDetails(models.Model):
    HIGH,MEDIUM,LOW="H","M","L"
    PRIORITY_OPTIONS=(
        (HIGH, "High"),
        (MEDIUM,"Medium"),
        (LOW,"Low"),
    )
    
    task=models.OneToOneField(Task,on_delete=models.CASCADE,related_name="details")
    priority=models.CharField(max_length=1,choices=PRIORITY_OPTIONS,default=LOW,)
    asset = models.ImageField(upload_to='task_asset',blank=True,null=True,default="task_asset/default_img.png")
    notes=models.TextField(blank=True,null=True)


    def __str__(self):
        return f"Details form of {self.task.title}"

class Project(models.Model):
    name = models.CharField(max_length=250)
    descriptions = models.TextField(blank=True,null=True)
    start_date = models.DateField()


    def __str__(self):
        return self.name


@receiver(post_save,sender=Task)
def task_creation_notification(sender,instance,**kwargs):
    print('sender',sender)
    print('instance',instance)
    print(kwargs)

