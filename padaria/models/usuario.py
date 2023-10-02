from django.db import models

from padaria.models import Endereco
from uploader.models import Image

class Usuario(models.Model):

    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.FloatField(max_length=11, null=True, blank=True)
    senha = models.CharField(max_length=50, null=False, blank=False)

    imagem = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True)
    endereco_padrao = models.ForeignKey(Endereco, on_delete=models.PROTECT, related_name="usuarios")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"