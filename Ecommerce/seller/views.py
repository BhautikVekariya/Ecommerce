from django.shortcuts import render
from mainapp.models import Product
# Create your views here.

def myProducts(request):
    seller = request.user 
    products = Product.objects.filter(seller = seller)
    template = 'products.html'
    context = {
        'products' : products,
        'seller' : True if request.user.user_profile.user_role == 'seller' else False
    }
    return render(request, template, context)
