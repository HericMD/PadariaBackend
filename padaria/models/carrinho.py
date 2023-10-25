from django.db import models

from padaria.models import Item, Endereco

class Carrinho(models.Model):

    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT, related_name="endereco")
    item = models.ManyToManyField(Item, related_name="item")

    def __str__(self):
        return f"{self.endereco} {self.item}"

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"