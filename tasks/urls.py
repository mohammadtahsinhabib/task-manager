from django.urls import path
from tasks.views import manager_dashboard,user_dashboard


urlpatterns = [
    path("admin-dashboard/",manager_dashboard),
    path("user-dashboard/",user_dashboard),

]
