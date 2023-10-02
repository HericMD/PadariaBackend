from django.db import models

from uploader.models import Image

class Categoria(models.Model):
    descricao = models.CharField(max_length=50, null=True, blank=True)
    imagem = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"