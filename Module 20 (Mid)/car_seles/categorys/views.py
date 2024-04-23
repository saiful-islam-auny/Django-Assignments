from django.shortcuts import render
from post.models import Car
from categorys.models import Category

def home(request, category_slug=None):
    data = Car.objects.all()
    categories = Category.objects.all()  # Rename the variable to avoid conflicts
    
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        data = Car.objects.filter(brand_name=category)
        
    return render(request, 'home.html', {'categories': categories, 'data': data})
