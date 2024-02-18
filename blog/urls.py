from django.urls import path, include

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_page, name='blog_page'),
    path('<slug:post_url>/', views.post_detail, name='post_detail')
]
