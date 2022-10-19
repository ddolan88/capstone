# from django.shortcuts import render
from django.views.generic import CreateView
# from django.contrib.auth.forms import(
#     UserCreationForm
#     # LoginForm
# )
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
    # class LoginView():
    #     form_class = LoginForm
    #     template_name = 'registration/login.html'
    #     success_url = reverse_lazy('login')