from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewCart, name='my_cart'),
    path('add/<int:product_id>', views.addToCart, name='add_to_cart')

]