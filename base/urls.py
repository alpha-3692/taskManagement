# base/urls.py

from django.urls import path

from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('', TaskListView.as_view(), name='tasks'),
    path('', TaskListView.as_view(), name='tasks'),
    # When the 'task/<int:pk>/' URL is requested, Django will serve the TaskDetailView for the task with the given primary key
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('add-new/', TaskCreateView.as_view(), name='add-new'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    # path('', views.note_list, name='note_list'),

]