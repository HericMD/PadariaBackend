from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from padaria.models import Carrinho
from padaria.serializers import CarrinhoSerializer


class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer