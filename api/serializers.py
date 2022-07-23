from rest_framework.serializers import ModelSerializer
from accounts.models import Customer, Order, Product
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class OrderSerializer(ModelSerializer):

  
    class Meta:
        model = Order
        fields = '__all__'
     

  
class ProductSerializer(ModelSerializer):
      class Meta:
        model=Product
        fields='__all__'

class CustomerSerializer(ModelSerializer):
      class Meta:
        model=Customer
        fields='__all__'

class UserSerializer(ModelSerializer):
  class Meta:
    model=User
    fields='__all__'
  
  def validate_password(self, value: str) -> str:
    """
    Hash value passed by user.

    :param value: password of a user
    :return: a hashed version of the password
    """
    return make_password(value)


