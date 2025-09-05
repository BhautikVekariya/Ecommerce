from django.contrib import admin
from .models import Product, Order, CartItem

# ---- Product Admin ----
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock")
    search_fields = ("name",)
    list_filter = ("stock",)

# ---- Order Admin ----
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "total_price", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__username",)

# ---- Cart Item Admin ----
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "quantity")
    list_filter = ("user",)
    search_fields = ("product__name", "user__username")
