from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.CharField(max_length=50, null=False, blank=False)
    preco = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Produtos"