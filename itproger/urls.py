from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('weather/', include('weather.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL) # я добавил эту строчку сюда, чтобы работал background, который у меня и так работал. также в settings.py я добавил некие настройки, которые выделил для возможного удаления, ибо и так всё работало.
