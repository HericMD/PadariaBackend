from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from padaria.models import Produto
from padaria.serializers import ProdutoSerializer, ProdutoListSerializer, ProdutoDetailSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categoria"] 
