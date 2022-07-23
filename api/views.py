from api.serializers import OrderSerializer,ProductSerializer,CustomerSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Customer, Order,Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User


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


@api_view(['GET'])
def getCustomers(request):
    customer=Customer.objects.all()
    serializer = CustomerSerializer(customer,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def placeOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def setCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

 # Get user 
@api_view(['GET'])
def getUser(request):
    routes = [
        "/api/token",
        "/api/token/refresh"
    ]
    return Response(routes)
  

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['password']= user.password

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['POST'])
def registerUser(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
    

