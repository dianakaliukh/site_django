from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('site_django.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

# Цей блок обов'язково має бути в кінці файлу
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)