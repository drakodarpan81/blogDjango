from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='index'),
    path('generales/', generales, name='generales'),
    path('programacion/', programacion, name='programacion'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('tutoriales/', tutoriales, name='tutoriales'),
    path('video_juegos/', video_juegos, name='video_juegos'),
    path('<slug:slug>/', detallePost, name='detalle_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
