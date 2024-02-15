from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth import get_user_model

from .forms import LoginUserForm, RegisterUserForm, UpdateProfileForm


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
        context['title'] = f'Профиль {self.object.username}'
        return context


class UpdateProfile(UpdateView):
    model = get_user_model()
    template_name = 'users/update_profile.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('home')
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля {self.object.username}' 
        return context
    
    # После успешного изменения профиля производится перенаправление на страницу профиля
    def get_success_url(self):
        return reverse('user:profile', kwargs={'pk': self.object.id})
    
    # Проверка на то, что пользователь может редактировать только свои профили
    def get(self, request, *args, **kwargs):
        if request.user.id != kwargs['pk']:
            return redirect('home')
        return super().get(request, *args, **kwargs)


def logout_user(request):
    logout(request)
    return redirect('home')
