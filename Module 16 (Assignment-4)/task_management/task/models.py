from django.db import models
from category.models import TaskCategory

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255, verbose_name="Task Title")
    taskDescription = models.TextField(verbose_name="Task Description")
    is_completed = models.BooleanField(default=False, verbose_name="Completed")
    taskAssignDate = models.DateField(verbose_name="Task Date")
    categories = models.ManyToManyField(TaskCategory, verbose_name="Task Categories")

    def __str__(self):
        return self.taskTitle