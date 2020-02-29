from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
   
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    rating = models.IntegerField(choices=RATING_CHOICES)
    
    
    def __str__(self):
        return self.comment