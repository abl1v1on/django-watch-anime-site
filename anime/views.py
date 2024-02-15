from django.shortcuts import get_object_or_404, redirect, render

from .models import Anime, Genre, Status, Comments
from .forms import CreateCommentForm


def index(request):
    anime_list = Anime.objects.all()

    context = {
        'title': 'Главаня страница',
        'anime': anime_list
    }
    return render(request, 'index.html', context)


def anime_detail(request, slug):
    anime = get_object_or_404(Anime, slug=slug)
    current_episode = request.GET.get('episode')
    episodes_count = [i for i in range(1, len(anime.anime_series.all()) + 1)]

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('user:login')
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comments.objects.create(
                user_id = request.user.id,
                anime_id = anime.id,
                comment_text = cd['comment_text']
            )
            return redirect('anime:anime_detail', slug=slug)
    else:
        form = CreateCommentForm
        if not current_episode:
            video = anime.anime_series.all()[0]
        else:
            if int(current_episode) <= len(episodes_count):
                video = anime.anime_series.all()[int(current_episode) - 1]
            else:
                return redirect('anime:anime_detail', slug=slug)

        context = {
            'title': anime.title,
            'anime': anime,
            'video': video,
            'episodes_count': episodes_count,
            'form': form,
            'comments': Comments.objects.filter(anime_id=anime.id).order_by('-id')
        }
    return render(request, 'anime/anime-details.html', context)


def anime_by_genre(request, genre_url):
    genre = get_object_or_404(Genre, slug=genre_url)

    context = {
        'title': f'Аниме в жанре {genre.genre_name}',
        # 'genre': genre,
        'anime': genre.anime_genre.all()
    }
    return render(request, 'categories.html', context)


def anime_by_status(request, status_url):
    status = get_object_or_404(Status, slug=status_url)

    context = {
        'title': f'{status.status_name}',
        'anime': status.anime_status.all()
    }
    return render(request, 'categories.html', context)
