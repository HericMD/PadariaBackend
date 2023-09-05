from django.db import models

class Endereco(models.Model):
    numero = models.FloatField(max_length=6, null=False, blank=False)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cep = models.FloatField(max_length=8, null=False, blank=False)

    def __str__(self):
        return f"{self.numero} {self.complemento} {self.cep}"

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"