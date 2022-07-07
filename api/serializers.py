from rest_framework.serializers import ModelSerializer
from accounts.models import Order, Product

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

  
class ProductSerializer(ModelSerializer):
      class Meta:
        model=Product
        fields='__all__'
