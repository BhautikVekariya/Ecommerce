# this file is for building custom forms.

# importing the User model from django's inbuilt authentication app
from django.contrib.auth.models import User 

from .models import Profile

# importing the inbuilt forms
from django import forms

# import AuthenticationForm from django's inbuilt authentication
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your username'
        })
    )

    password = forms.CharField(
        label = 'Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your password'
        })
    )

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username','email','password1','password2')
    email = forms.EmailField(
        widget= forms.EmailInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your email'
        })
    )
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your username',
            
        })
    )

    password1 = forms.CharField(
        label = 'Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your password'
        })
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Confirm Password'
        })
    )


class CustomProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','profile_photo','last_name','email','user_role','phone_number','address')
        template_name='authentication/add_profile.html'
        success_url='/'


class CustomProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','email','phone_number','address','profile_photo')
        template_name='authentication/add_profile.html'
        success_url='/'

    