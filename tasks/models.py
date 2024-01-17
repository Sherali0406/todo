from django.db import models
from django.utils import timezone


class Task(models.Model):
    EXMP_CHOICES = [
        ('todo', 'To Do'),
        ('in progress', 'In Progress'),
        ('done', 'Done')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(default="description...")
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=EXMP_CHOICES, default='todo')  

    def __str__(self) -> str:
        return self.title
