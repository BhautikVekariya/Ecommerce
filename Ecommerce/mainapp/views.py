from django.shortcuts import render

from django.views.generic import CreateView, ListView, DetailView,UpdateView,DeleteView

from . models import Product
from django.urls import reverse_lazy

from .forms import ProductForm
# Create your views here.
# def homeView(request):
#     template = 'home.html'
#     context={
#        'products': Product.objects.all()
#     }
#     return  render(request, template, context)

class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['seller'] = True if self.request.user.user_profile.user_role == 'seller' else False
        return context

def aboutView(request):
    template = 'about.html'
    context={
       
    }
    return  render(request, template, context)


def contactView(request):
    template = 'contact.html'
    context = {

    }
    return render(request, template, context)


def productsView(request):
    template = 'products.html'
    context = {
        'products' : Product.objects.all(),
        'seller' : True if request.user.user_profile.user_role == 'seller' else False
    }
    return render(request, template, context)



class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['seller'] = True if self.request.user.user_profile.user_role == 'seller' else False
        return context
    
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class ProductDetails(DetailView):
    model = Product
    template_name = 'prod_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['seller'] = True if self.request.user.user_profile.user_role == 'seller' else False
        return context

class UpdateProduct(UpdateView):
    model = Product
    template_name = 'update_product.html'
    fields = '__all__'
    success_url = '/'

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = '/'

class EditProduct(UpdateView):
    model=Product
    fields='__all__'
    template_name='edit_product.html'
    success_url=reverse_lazy('homepage')

def searchView(request):
    query = request.GET.get('q')
    result_products = Product.objects.filter(title__icontains = query)
    context = {
        'query' : query,
        'products' : result_products
    }
    template = 'search_results.html'

    return render(request, template, context)