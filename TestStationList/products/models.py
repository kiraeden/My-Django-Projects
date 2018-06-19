from django.db import models
from django.db.models.fields import CharField

class Products(models.Model):
    product_name = CharField(max_length=50)
    
    def __str__(self):
        return product_name