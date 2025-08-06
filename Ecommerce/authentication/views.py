from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User 


from django.urls import reverse_lazy

# importing custom form
from .forms import CustomLoginForm, CustomRegisterForm

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm

class CustomRegisterView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'register.html'
    # find the sign-in page path on successful registration and send the user there
    success_url = reverse_lazy('signin') 