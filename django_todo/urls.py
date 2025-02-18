"""
URL configuration for django_todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""


# django_todo/urls.py

from django.contrib import admin
from django.urls import include, path

from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls')),
    path('', views.index, name='index'),  # Add this line for the root path
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('task_list/', views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]


