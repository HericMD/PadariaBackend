from django.db import models

from padaria.models import Produto, Usuario

class Carrinho(models.Model):

    numero = models.FloatField(max_length=6, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    rua = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    cep = models.FloatField(max_length=8, null=True, blank=True)
    
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="produto")
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="usuario")

    def __str__(self):
        return f"{self.usuario} - {self.produto}"

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"