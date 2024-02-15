from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('signup/', views.RegisterUserView.as_view(), name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>/', views.UserProfile.as_view(), name='profile'),
]
