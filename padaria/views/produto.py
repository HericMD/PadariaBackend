from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from padaria.models import Produto
from padaria.serializers import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer