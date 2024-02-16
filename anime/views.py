from django.shortcuts import get_object_or_404, redirect, render

from .models import Anime, Genre, Status, Comments
from .forms import CreateCommentForm
from .utils import get_all_anime, create_comment, get_comments_by_anime_id


def index(request):
    anime_list = get_all_anime().order_by('-id')

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
            create_comment(request.user.id, anime.id, cd['comment_text'])
            return redirect('anime:anime_detail', slug=slug)
    else:
        form = CreateCommentForm()

        if not current_episode:
            try:
                video = anime.anime_series.all()[0]
            except IndexError:
                video = ''
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
            'comments': get_comments_by_anime_id(anime.id).order_by('-id')
        }
    return render(request, 'anime/anime-details.html', context)


def anime_by_genre(request, genre_url):
    genre = get_object_or_404(Genre, slug=genre_url)
    anime = genre.anime_genre.all()

    sort_by = request.GET.get('sort_by', None)

    if sort_by:
        if sort_by == 'date_aired':
            anime = anime.order_by('-date_aired')
        if sort_by == 'views':
            anime = anime.order_by('-views')


    context = {
        'title': f'Аниме в жанре {genre.genre_name}',
        'anime': anime
    }
    return render(request, 'categories.html', context)


def anime_by_status(request, status_url):
    status = get_object_or_404(Status, slug=status_url)

    context = {
        'title': f'{status.status_name}',
        'anime': status.anime_status.all()
    }
    return render(request, 'categories.html', context)
