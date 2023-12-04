from django.db import models
from padaria.models import Produto

class Item(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="item", default =1)
    quantidade = models.IntegerField(default = 1)

    def __str__(self):
        return f"{self.produto} {self.quantidade}"

    class Meta:
        verbose_name_plural = "Itens"
