from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import ToDoSerializer

class Tasks(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = ToDoSerializer

    @action(detail=False, methods=['GET'])
    def completed(self, request):
        queryset = Task.objects.filter(status='done')
        serializer = self.get_serializer(queryset, many=True) #olingan malumotlarni jsonga o'tkazish u-n
        return Response(serializer.data)

    @action(detail=False, methods=['GET']) 
    def inprogress(self, request):
        queryset = Task.objects.filter(status='in_progress')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def expired(self, request):
        queryset = Task.objects.filter(end_time__lt=timezone.now())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
