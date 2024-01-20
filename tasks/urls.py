from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import Tasks

router = DefaultRouter()
router.register(r'tasks', Tasks, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
