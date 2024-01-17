from django.utils import timezone  # Import the timezone module
from rest_framework import serializers

from tasks.models import Task

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    # You can customize the default or example values for each field
    title = serializers.CharField(default=" write a title ... ", )
    description = serializers.CharField(default=" write Description about your plan", )
    start_time = serializers.DateTimeField(default=timezone.now,)
    end_time = serializers.DateTimeField(default=timezone.now)
    status = serializers.ChoiceField(choices=Task.EXMP_CHOICES, default='todo', )
