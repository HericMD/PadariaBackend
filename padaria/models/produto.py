from django.db import models
from uploader.models import Image

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.CharField(max_length=50, null=False, blank=False)
    preco = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )


    def __str__(self):
        return f"{self.nome} {self.preco}"

    class Meta:
        verbose_name_plural = "Produtos"