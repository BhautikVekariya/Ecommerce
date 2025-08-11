from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from mainapp.models import Product
from django.contrib.auth.decorators import login_required

from .models import CartItem
# Create your views here.

def viewCart(request):
    template= 'my_cart.html'
    cart_items = CartItem.objects.filter(user = request.user)
    total_price = sum(item.sub_total for item in cart_items)
    context = {
        'items' : cart_items,
        'total_price' : total_price
    }
    return render(request, template, context)

@login_required
def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id)
    this_user = request.user 
    cart_item, created_at = CartItem.objects.get_or_create(product = this_product, user = this_user)
    cart_item.quantity += 1
    cart_item.save()
    
    return redirect(reverse_lazy('my_cart'))