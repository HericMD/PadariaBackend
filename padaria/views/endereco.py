from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from padaria.models import Endereco
from padaria.serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer