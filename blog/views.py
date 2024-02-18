from django.shortcuts import get_object_or_404, render

from .models import Blog


def blog_page(request):
    posts = Blog.objects.all()

    context = {
        'title': 'Наш блог',
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def post_detail(request, post_url):
    post = get_object_or_404(Blog, slug=post_url)

    context = {
        'title': post.title,
        'post': post
    }
    return render(request, 'blog/blog-details.html', context)
