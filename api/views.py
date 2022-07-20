from api.serializers import OrderSerializer,ProductSerializer,CustomerSerializer,RegisteredUsersSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Customer, Order,Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


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

@api_view(['POST'])
def placeOrder(request):
    data =  request.data
    order = Customer.objects.create(
        name=data['name'],
        phone=data['phone'],
        email=data['email'],
        country=data['country'],
        street=data['street'],
        state=data['state'],
        zipcode=data['zipcode'],
        cartnumber=data['cartnumber']
    )
    serializer =  CustomerSerializer(order, many=False)
    return Response(serializer.data)

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