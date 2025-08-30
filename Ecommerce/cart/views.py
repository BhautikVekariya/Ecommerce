from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from mainapp.models import Product
from .models import CartItem
from cart import views
print(dir(views))  # This will show all functions in views.py

# Create your views here.

def view_cart(request):
    template = 'my_cart.html'
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.sub_total for item in cart_items)
    context = {
        'items': cart_items,
        'total_price': total_price
    }
    return render(request, template, context)

@login_required
def add_to_cart(request, product_id):
    this_product = Product.objects.get(id=product_id)
    this_user = request.user 
    cart_item, created = CartItem.objects.get_or_create(product=this_product, user=this_user)
    cart_item.quantity += 1
    cart_item.save()
    
    return redirect(reverse_lazy('my_cart'))

def remove_from_cart(request, cart_item_id):
    this_cart_item = CartItem.objects.get(id=cart_item_id)
    this_cart_item.delete()
    return redirect(reverse_lazy('my_cart'))

@require_POST
@login_required
def update_quantity(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
        is_add = request.POST.get('is_add') == 'True' or request.POST.get('is_add') == 'true'
        
        if is_add:
            cart_item.quantity += 1
        else:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                cart_item.delete()
                return JsonResponse({
                    'status': 'removed',
                    'overall_total': sum(item.sub_total for item in CartItem.objects.filter(user=request.user))
                })
        
        cart_item.save()
        
        return JsonResponse({
            'status': 'success',
            'quantity': cart_item.quantity,
            'sub_total': cart_item.sub_total,
            'overall_total': sum(item.sub_total for item in CartItem.objects.filter(user=request.user))
        })
    except CartItem.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Item not found'})