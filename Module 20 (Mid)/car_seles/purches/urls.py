from django.urls import path 
from .views import buy_car 
 
urlpatterns = [ 
   
    path('buy_car/<int:car_id>/', buy_car, name='buy_now'), 
]