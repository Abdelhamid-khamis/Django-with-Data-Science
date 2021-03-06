from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# We here created a table(model) called Products
class Product(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
       
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True)
    salesman = models.ForeignKey(User, on_delete=models.CASCADE)
    # change required for the below line
    date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity 
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Sold {self.quantity} items of {self.product.name}s for {self.price}."
    
        
    