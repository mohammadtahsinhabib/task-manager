from django.urls import path
from tasks.views import *


urlpatterns = [
    path("admin-dashboard/",manager_dashboard),
    path("user-dashboard/",user_dashboard),
    path("create-task/",create_task),

]
