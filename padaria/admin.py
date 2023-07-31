from django.contrib import admin

from .models import Carrinho, Endereco, Produto, Usuario

admin.site.register(Carrinho)
admin.site.register(Endereco)
admin.site.register(Produto)
admin.site.register(Usuario)