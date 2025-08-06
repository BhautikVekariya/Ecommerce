from django.urls import path
from .views import CustomLoginView, CustomRegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'signup'),
    path('register/', CustomRegisterView.as_view(), name = 'register')
]