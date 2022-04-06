from django.shortcuts import render, get_object_or_404
from .models import *


def Home(request):
    posts = Post.objects.filter(estado=True)
    data = {
        'posts': posts
    }
    return render(request, 'index.html', data)


def detallePost(request, slug):
    posts = Post.objects.get(slug=slug)

    data = {
        'detalle_posts': posts
    }
    # post = get_object_or_404(Post, slug=slug) # Funciona igual que la consulta, pero valida si existe o no
    return render(request, 'post.html', data)


def generales(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Generales'))

    data = {
        'posts': posts
    }
    return render(request, 'generales.html', data)


def programacion(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Programación'))

    data = {
        'posts': posts
    }
    return render(request, 'programacion.html', data)


def tutoriales(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Tutoriales')
    )

    data = {
        'posts': posts
    }

    return render(request, 'tutoriales.html', data)


def tecnologia(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Tecnología')
    )

    data = {
        'posts': posts
    }
    return render(request, 'tecnologia.html', data)


def video_juegos(request):
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Video juegos')
    )

    data = {
        'posts': posts
    }
    return render(request, 'videojuegos.html', data)
