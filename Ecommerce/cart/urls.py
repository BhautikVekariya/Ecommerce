from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='my_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='rem_from_cart'),
    path('update-quantity/<int:cart_item_id>/', views.update_quantity, name='update_quantity'),
]