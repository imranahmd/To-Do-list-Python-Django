from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
