from .models import Anime, Comments


def get_all_anime():
    return Anime.objects.all()


def create_comment(user_id, anime_id, text):
    Comments.objects.create(
        user_id = user_id,
        anime_id = anime_id,
        comment_text = text
    )

def get_all_comments():
    return Comments.objects.all()


def get_comments_by_anime_id(anime_id):
    return Comments.objects.filter(anime_id=anime_id)


def get_recomendation_anime(anime):
    recomendations = []
    for a in get_all_anime():
        if a.title != anime.title:
            for genre in a.genre.all():
                if genre in anime.genre.all():
                    recomendations.append(a)
                    break
    return recomendations
