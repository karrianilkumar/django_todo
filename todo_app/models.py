from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

