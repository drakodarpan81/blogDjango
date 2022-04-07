from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator


def Home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True)

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    data = {
        'posts': posts
    }
    return render(request, 'index.html', data)


def detallePost(request, slug):
    # Funciona igual que la consulta, pero valida si existe o no
    posts = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'detalle_posts': posts})


def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Generales'))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Generales'))

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    data = {
        'posts': posts
    }
    return render(request, 'generales.html', data)


def programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Programación'))

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Programación'))

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    data = {
        'posts': posts
    }
    return render(request, 'programacion.html', data)


def tutoriales(request):
    queryset = request.Get.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Tutoriales')
    )

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Tutoriales')
        )

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    data = {
        'posts': posts
    }

    return render(request, 'tutoriales.html', data)


def tecnologia(request):
    queryset = request.Get.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Tecnología')
    )

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Tecnología')
        )

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    data = {
        'posts': posts
    }
    return render(request, 'tecnologia.html', data)


def video_juegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='Video juegos')
    )

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Video juegos')
        )

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    data = {
        'posts': posts
    }
    return render(request, 'videojuegos.html', data)
