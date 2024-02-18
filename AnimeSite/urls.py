from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from anime.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('anime/', include('anime.urls', namespace='anime')),
    path('user/', include('users.urls', namespace='user')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    