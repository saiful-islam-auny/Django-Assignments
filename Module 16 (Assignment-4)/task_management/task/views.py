from django.shortcuts import render,redirect
from . import forms
from . import models
def add_task(request):
    if request.method == 'POST': 
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid(): 
            task_form.save() 
            return redirect('taskpage') 
    
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form' : task_form})


def edit_task(request, id):
    task = models.TaskModel.objects.get(pk=id) 
    task_form = forms.TaskForm(instance=task)
    # print(post.title)
    if request.method == 'POST': # user post request koreche
        task_form = forms.TaskForm(request.POST, instance=task) # user er post request data ekhane capture korlam
        if task_form.is_valid(): # post kora data gula amra valid kina check kortechi
            task_form.save() # jodi data valid hoy taile database e save korbo
            return redirect('taskpage') # sob thik thakle take add author ei url e pathiye dibo
    
    return render(request, 'add_task.html', {'form' : task_form})

def delete_task(request, id):
    task = models.TaskModel.objects.get(pk=id) 
    task.delete()
    return redirect('taskpage')