from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('about/', views.aboutView, name='aboutpage'),
    path('products/', views.productsView, name='products'),
    path('contact/', views.contactView, name='contact'),
    path('product/add/', views.AddProduct.as_view(), name='add_product'),
    path('product/<int:pk>', views.ProductDetails.as_view(), name= 'prod_details'),
    path('product/update/<int:pk>', views.UpdateProduct.as_view(), name = 'updateproduct'),
    path('product/edit/<int:pk>', views.EditProduct.as_view(),name='edit_product'),
    path('product/delete/<int:pk>', views.DeleteProduct.as_view(), name = 'deleteproduct'),
      path('search/', views.searchView, name = 'search_products')
]