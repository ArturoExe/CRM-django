from pyexpat import model
from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created_on=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
         return self.name


class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    
    def __str__(self):
         return self.name

class Product(models.Model):

    CATEGORY=(
    ('Out door','Out door'),
    ('Indoor','Indoor'), 
    )

    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    description=models.TextField(null=True,blank=True)
    date_created_on=models.DateTimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tag)


    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS=(
    ('Pending','Pending'),
    ('Out for delivery','Out for delivery'),
    ('Delivered','Delivered'),
    ('Returned','Returned')
    )


    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL) 
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created_on=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    note = models.CharField(max_length=1000,null=True)
    def __str__(self):
         return self.product.name
