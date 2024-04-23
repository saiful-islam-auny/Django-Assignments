from django.shortcuts import render 
from django.contrib import messages 
# Create your views here. 
 
from django.shortcuts import get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required 
from .models import Car, Purchase 
from django.views import View 
 
@login_required 
def buy_car(request, car_id): 
    car_instance = get_object_or_404(Car, id=car_id) 
 
    if car_instance.quantity > 0: 
        
        car_instance.quantity -= 1 
        car_instance.save() 
 
     
        Purchase.objects.create(user=request.user, car=car_instance)


        messages.success(request, 'Buy car successfully') 
        return redirect('profile') 
 
    return render(request, 'error.html', {'error_message': 'Not enough quantity available'})