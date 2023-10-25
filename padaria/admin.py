from django.contrib import admin

from .models import Carrinho, Endereco, Produto, Categoria, Item

admin.site.register(Carrinho)
admin.site.register(Categoria)
admin.site.register(Endereco)
admin.site.register(Produto)
admin.site.register(Item)