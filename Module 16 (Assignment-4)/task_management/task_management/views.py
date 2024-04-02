from django.shortcuts import render
from task.models import TaskModel


def show(request):
    data = TaskModel.objects.all()
    return render(request, 'show.html', {'data' : data})