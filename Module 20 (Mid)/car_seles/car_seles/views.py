from django.shortcuts import render 
from categorys.models import Category 
from post.models import Car 

def home(request,brand_slug=None): 
    data = Car.objects.all()  
    if brand_slug is not None:  
        selected_brand = Category.objects.get(slug = brand_slug)  
        data = Car.objects.filter(brand_name= selected_brand)  
    brands = Category.objects.all()  
    return render(request, 'home.html', {'data' : data, 'brand_list' :brands})