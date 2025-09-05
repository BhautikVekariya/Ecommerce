from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Order, Product, CartItem

# ---- USER DASHBOARD ----
@login_required
def user_dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    cart_items = CartItem.objects.filter(user=request.user)

    return render(request, "dashboard/user_dashboard.html", {
        "orders": orders,
        "cart_items": cart_items,
    })

# ---- ADMIN DASHBOARD ----
@login_required
def admin_dashboard(request):
    total_users = User.objects.count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    recent_orders = Order.objects.select_related("user", "product").order_by("-created_at")[:5]

    return render(request, "dashboard/admin_dashboard.html", {
        "total_users": total_users,
        "total_products": total_products,
        "total_orders": total_orders,
        "recent_orders": recent_orders,
    })