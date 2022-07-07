from django.db import models

# Create your models here.
class RegisteredUsers(models.Model):
     customerName= models.CharField(max_length=100,null=True)
     customerPassword = models.CharField(max_length=100,null=True)
    

     def __str__(self):
         return self.customerName
