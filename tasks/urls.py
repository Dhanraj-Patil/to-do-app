from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update/<int:pk>/', views.updateTask, name="update_task"),
    path('delete/<int:pk>/', views.deleteTask, name="delete_task")
]