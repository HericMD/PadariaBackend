from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from padaria.models import Categoria
from padaria.serializers import CategoriaSerializer, CategoriaListSerializer, CategoriaDetailSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CategoriaListSerializer
        elif self.action == "retrieve":
            return CategoriaDetailSerializer
        return CategoriaSerializer