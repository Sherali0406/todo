from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from .views import (CreateToDo, DeleteToDo, DetailToDo, ListToDo,
                    ListToDoByStatus, ListToDoCompleted, ListToDoExpired,
                    ListToDoInprogress, PartialUpdateToDo, UpdateToDo)

urlpatterns = [
    path('swagger_ui/', TemplateView.as_view(
        extra_context={'schema_url': 'api'}
    ), name='swagger-ui'),
    
    path('api',get_schema_view(title='API Schema',description='Guide for the REST API'),name='api'),
    path('api/tasks/create', CreateToDo.as_view(), name='task-create'),
    path('api/tasks/', ListToDo.as_view(), name='task-list'),
    path('api/tasks/detail<int:pk>/', DetailToDo.as_view(), name='task-detail'),
    path('api/tasks/update-full/<int:pk>/', UpdateToDo.as_view(), name='task-update'),
    path('api/tasks/update-partial<int:pk>/', PartialUpdateToDo.as_view(), name='task-partial-update'),
    path('api/tasks/delete/<int:pk>/', DeleteToDo.as_view(), name='task-delete'),
    path('api/tasks/expired/', ListToDoExpired.as_view(), name='task-list-expired'),
    path('api/tasks/in_progress/', ListToDoInprogress.as_view(), name='task-list-in-progress'),
    path('api/tasks/done/', ListToDoCompleted.as_view(), name='task-list-done'),
    path('api/tasks/to-do/<str:status>/', ListToDoByStatus.as_view(), name='task-list-todo'),
]
