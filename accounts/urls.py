from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('products/', views.products,name='products'),
    path('customer/<str:pk_test>', views.customer,name='customer'),
    path('place_order/<str:pk>/', views.placeOrder,name='place_order'),
    path('update_order/<str:pk>/', views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder,name='delete_order'),

]
