from django.db import models
from django.contrib.auth.models import User
from post.models import Car

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase #{self.id} by {self.user.username} for {self.quantity} {self.car.name}(s)"
