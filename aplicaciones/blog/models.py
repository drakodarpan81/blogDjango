from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombre = models.CharField(
        _("Nombre de la categoria"), max_length=100, blank=False, null=False)
    estado = models.BooleanField(
        _("Categoria Activada/Categoria no Activada"), default=True)
    fecha_creacion = models.DateField(
        _("Fecha de creación"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("Categoria")
        verbose_name_plural = _("Categorias")
        ordering = ["id"]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Categoria_detail", kwargs={"pk": self.pk})


class Autor(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombres = models.CharField(
        _("Nombres de autores"), max_length=255, null=False, blank=False)
    apellidos = models.CharField(
        _("Apellidos"), max_length=255, null=False, blank=False)
    facebook = models.URLField(_("Facebook"), null=True, blank=True)
    twitter = models.URLField(_("Twitter"), null=True, blank=True)
    instagram = models.URLField(_("Instagram"), null=True, blank=True)
    web = models.URLField(_("Web"), null=True, blank=True)
    correoelectronico = models.EmailField(
        _("Correo Electronico"), max_length=254, null=False, blank=False)
    estado = models.BooleanField(
        _("Autor Activo/Autor no Activo"), default=True)
    fecha_creacion = models.DateField(
        _("Fecha de creación"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("Autor")
        verbose_name_plural = _("Autores")
        ordering = ['id']

    def __str__(self):
        return "{0} , {1}".format(self.apellidos, self.nombres)

    def get_absolute_url(self):
        return reverse("Autor_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    titulo = models.CharField(
        _("Titulo"), max_length=90, blank=False, null=False)
    slug = models.CharField(_("Slug"), max_length=100, blank=False, null=False)
    descripcion = models.CharField(
        _("Descripción"), max_length=110, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.URLField(
        _("Imagen"), max_length=200, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(_("Publicado/Sin publicar"), default=True)
    fecha_creacion = models.DateField(
        _("Fecha de creación"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
