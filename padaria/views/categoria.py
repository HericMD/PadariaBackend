from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from padaria.models import Categoria
from padaria.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer