# Generated by Django 4.0.2 on 2022-04-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombres', models.CharField(max_length=255, verbose_name='Nombres de autores')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('correoelectronico', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('estado', models.BooleanField(default=True, verbose_name='Autor Activo/Autor no Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autors',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria Activada/Categoria no Activada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
    ]
