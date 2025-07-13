import os
import django
import random
from datetime import timedelta, date

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_management.settings")
django.setup()

from tasks.models import Task, TaskDetails, Project
from django.contrib.auth.models import User

# Create 10 users if not already created
if User.objects.count() < 10:
    for i in range(10):
        User.objects.create_user(username=f"user{i}", password="password")

users = list(User.objects.all())

# Create 5 projects if not already created
if Project.objects.count() < 5:
    for i in range(5):
        Project.objects.create(
            name=f"Project {i}",
            descriptions="Auto-generated project",
            start_date=date.today() - timedelta(days=random.randint(10, 100))
        )

projects = list(Project.objects.all())

statuses = ["PENDING", "IN_PROGRESS", "COMPLETED"]
priorities = ["H", "M", "L"]

# Create 300 tasks
for i in range(300):
    task = Task.objects.create(
        title=f"Task {i}",
        descriptions="This is an auto-generated task.",
        due_date=date.today() + timedelta(days=random.randint(1, 30)),
        status=random.choice(statuses),
        project=random.choice(projects)
    )
    task.assigned_to.set(random.sample(users, random.randint(1, 3)))

    TaskDetails.objects.create(
        task=task,
        priority=random.choice(priorities),
        notes="Auto-generated notes"
    )

print("✅ 300+ tasks created successfully.")
