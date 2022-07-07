from . import views 
from django.urls import path

urlpatterns = [
    path('', views.getCart, name='cart'),
    path('cart/<str:pk>',views.getOrder,name='order'),
    path('cart/',views.getOrders,name='orders'),
    path('products/',views.getProducts,name='products')

]
