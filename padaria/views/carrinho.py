from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from padaria.models import Carrinho
from padaria.serializers import CarrinhoSerializer, CarrinhoListSerializer, CarrinhoDetailSerializer


class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CarrinhoListSerializer
        elif self.action == "retrieve":
            return CarrinhoDetailSerializer
        return CarrinhoSerializer