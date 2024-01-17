from django.utils import timezone
from rest_framework import generics
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from .models import Task
from .serializers import ToDoSerializer


class ListToDo(generics.ListAPIView):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date:
            queryset = queryset.filter(start_time__gte=start_date)
        if end_date:
            queryset = queryset.filter(end_time__lte=end_date)

        return queryset

class DetailToDo(RetrieveAPIView):         #by id
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer

class CreateToDo(generics.CreateAPIView): #create smth
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer

class UpdateToDo(UpdateAPIView):  #update smth
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer

class PartialUpdateToDo(generics.UpdateAPIView):  # Using UpdateAPIView for partial updates
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer

class DeleteToDo(DestroyAPIView):  #delete smth
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer


class ListToDoByStatus(generics.ListAPIView):  #get by statusss 
    serializer_class = ToDoSerializer

    def get_queryset(self):
        status = self.kwargs['status']
        return Task.objects.filter(status=status)


class ListToDoCompleted(generics.ListAPIView):  #sort by done
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return Task.objects.filter(status='done')
    

class ListToDoInprogress(generics.ListAPIView):  #sort by in_progress
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return Task.objects.filter(status='in_progress')

class ListToDoExpired(generics.ListAPIView):  
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return Task.objects.filter(end_time__lt=timezone.now())
