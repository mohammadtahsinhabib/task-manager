from django.urls import path
from tasks.views import *


urlpatterns = [
    path("admin-dashboard/",manager_dashboard,name="manager-dashboard"),
    path("user-dashboard/",user_dashboard,name="user-dashboard"),
    path("create-task/",create_task,name="create-task"),
    path("update-task/<int:id>/",update_task,name="update-task"),
    path("view-task/",view_task),
    path("task/<int:task_id>/details/", task_details, name="task-details"),
    path("delete-task/<int:id>/",delete_task,name="delete-task"),
    path("dashboard/",dashboard,name="dashboard"),
]
