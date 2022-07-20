import imp
from api.models import RegisteredUsers
from rest_framework.serializers import ModelSerializer
from accounts.models import Customer, Order, Product
from api.models import RegisteredUsers

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

class RegisteredUsersSerializer(ModelSerializer):
      class Meta:
        model=RegisteredUsers
        fields='__all__'