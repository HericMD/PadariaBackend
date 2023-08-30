from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from padaria.models import Usuario
from padaria.serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer