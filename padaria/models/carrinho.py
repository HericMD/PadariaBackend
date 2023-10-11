from django.db import models

from padaria.models import Produto, Endereco

class Carrinho(models.Model):

    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT, related_name="produto")
    produto = models.ManyToManyField(Produto, related_name="produto")

    def __str__(self):
        return f"{self.endereco} - {self.produto}"

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"