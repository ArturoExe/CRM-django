from api.serializers import OrderSerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Order,Product
from api import serializers

@api_view(['GET'])
def getCart(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

# Get all orders
@api_view(['GET'])
def getOrders(request):
    orders=Order.objects.all()
    serializer = OrderSerializer(orders,many=True)
    return Response(serializer.data)


# Get a single order by ID
@api_view(['GET'])
def getOrder(request,pk):
    order =  Order.objects.get(id=pk)
    serializer = OrderSerializer(order,many=False)
    return Response(serializer.data)


# Get all products
@api_view(['GET'])
def getProducts(request):
    products=Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)
