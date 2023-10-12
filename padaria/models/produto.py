from django.db import models
from uploader.models import Image
from padaria.models import Categoria

class Produto(models.Model):
    class Unidade(models.IntegerChoices):
        UNIDADE = (1, "Unidade",)
        PESO = (2, "Peso (KG)")
    nome = models.CharField(max_length=255, null=False, blank=False)
    preco = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    unidade = models.IntegerField(choices=Unidade.choices, default=Unidade.UNIDADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="produto", null=True, blank=True)
    imagem = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.preco}"

    class Meta:
        verbose_name_plural = "Produtos"
