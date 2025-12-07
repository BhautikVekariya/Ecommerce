from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from authentication.models import Profile
from .models import Product
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import ProductForm


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # SAFE PROFILE ACCESS
        profile = getattr(self.request.user, 'user_profile', None)
        context['seller'] = profile.user_role == 'seller' if profile else False

        return context


def aboutView(request):
    return render(request, 'about.html')


def contactView(request):
    return render(request, 'contact.html')


def productsView(request):
    context = {
        'products': Product.objects.all(),
    }

    # SAFE PROFILE ACCESS
    profile = getattr(request.user, 'user_profile', None)
    context['seller'] = profile.user_role == 'seller' if profile else False

    return render(request, 'products.html', context)


@login_required
def myproductsview(request):
    template = 'my_products.html'
    products = Product.objects.filter(user=request.user)

    context = {'products': products}

    profile = getattr(request.user, 'user_profile', None)
    context['user'] = profile.user_role == 'user' if profile else False

    return render(request, template, context)


class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # SAFE PROFILE ACCESS
        profile = getattr(self.request.user, 'user_profile', None)
        context['seller'] = profile.user_role == 'seller' if profile else False

        return context

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductDetails(DetailView):
    model = Product
    template_name = 'prod_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # SAFE PROFILE ACCESS
        profile = getattr(self.request.user, 'user_profile', None)
        context['seller'] = profile.user_role == 'seller' if profile else False

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
    model = Product
    fields = '__all__'
    template_name = 'edit_product.html'
    success_url = reverse_lazy('homepage')


def searchView(request):
    query = request.GET.get('q')
    result_products = Product.objects.filter(title__icontains=query)

    context = {
        'query': query,
        'products': result_products
    }

    return render(request, 'search_results.html', context)
