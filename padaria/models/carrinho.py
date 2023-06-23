from django.db import models

from padaria.models import Produto, Usuario

class Carrinho(models.Model):

    numero = models.FloatField(max_length=6, null=False, blank=False)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    rua = models.CharField(max_length=50, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    cep = models.FloatField(max_length=8, null=False, blank=False)

    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="carrinho1")
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="carrinho2")

    def __str__(self):
        return f"{self.usuario} {self.produto}"

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"