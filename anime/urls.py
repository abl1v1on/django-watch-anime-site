from django.urls import path

from . import views

app_name = 'anime'

urlpatterns = [
    path('<slug:slug>/', views.anime_detail, name='anime_detail'),
    path('genre/<slug:genre_url>/', views.anime_by_genre, name='anime_by_genre'),
    path('status/<slug:status_url>/', views.anime_by_status, name='anime_by_status'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment')
]
