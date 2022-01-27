import uuid
from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import AbstractUser, BaseUserManager


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class TipoReceita(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.descricao


class Receita(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoReceita, on_delete=models.CASCADE)
    ingredientes = models.TextField()
    preparo = models.TextField()
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        abstract = True

    def __str__(self):
        return self.titulo


class Entrada(Receita):

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'


class Principal(Receita):

    class Meta:
        verbose_name = 'Principal'
        verbose_name_plural = 'Principais'


class Sobremesa(Receita):

    class Meta:
        verbose_name = 'Sobremesa'
        verbose_name_plural = 'Sobremesas'