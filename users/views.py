from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth import get_user_model

from .forms import LoginUserForm, RegisterUserForm


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/signup.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация' 
        return context


class UserProfile(DetailView):
    model = get_user_model()
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        return context


def logout_user(request):
    logout(request)
    return redirect('home')
