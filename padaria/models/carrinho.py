from django.db import models

from padaria.models import Item, Endereco

class Carrinho(models.Model):

    endereco_carrinho = models.ForeignKey(Endereco, on_delete=models.PROTECT, related_name="endereco", null=True, blank=True)
    item = models.ManyToManyField(Item, related_name="item")

    def __str__(self):
        return f"{self.endereco_carrinho} {self.item}"

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"