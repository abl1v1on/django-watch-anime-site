from django.urls import path

from . import views

app_name = 'anime'

urlpatterns = [
    path('<slug:slug>/', views.anime_detail, name='anime_detail')
]
