from django.urls import path
from . import views

# todo_app/urls.py
urlpatterns = [
   # path('', views.task_list, name='task_list'),
    path('', views.index, name='index'),
    path('task_list/', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]





