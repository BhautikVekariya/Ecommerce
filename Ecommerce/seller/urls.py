from . import views
from django.urls import path


urlpatterns = [
    path('products/mine', views.myProducts, name='my_products'),
]