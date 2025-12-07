from django.shortcuts import render
from mainapp.models import Product

def myProducts(request):
    profile = getattr(request.user, 'user_profile', None)

    context = {
        'products': Product.objects.filter(seller=request.user),
        'seller': profile.user_role == 'seller' if profile else False
    }

    return render(request, 'seller/my_products.html', context)
