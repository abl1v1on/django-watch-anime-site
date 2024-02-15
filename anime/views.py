from django.shortcuts import get_object_or_404, render

from .models import Anime


def index(request):
    anime_list = Anime.objects.all()

    context = {
        'title': 'Главаня страница',
        'anime': anime_list
    }
    return render(request, 'index.html', context)


def anime_detail(request, slug):
    anime = get_object_or_404(Anime, slug=slug)
    episodes_count = [i for i in range(1, len(anime.anime_series.all()) + 1)]

    if not request.GET.get('episode'):
        video = anime.anime_series.all()[0]
    else:
        video = anime.anime_series.all()[int(request.GET.get('episode')) - 1]

    context = {
        'title': anime.title,
        'anime': anime,
        'video': video,
        'episodes_count': episodes_count
    }
    return render(request, 'anime/anime-details.html', context)
