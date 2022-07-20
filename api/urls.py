from . import views 
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import MyTokenObtainPairView


urlpatterns = [
    path('', views.getCart, name='cart'),
    path('cart/<str:pk>',views.getOrder,name='order'),
    path('cart/',views.getOrders,name='orders'),
    path('cart/order/place',views.placeOrder,name='place-order'),
    path('products/',views.getProducts,name='products'),
    path('user/',views.getUser,name='user'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
