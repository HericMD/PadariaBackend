from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from padaria.models import Item
from padaria.serializers import ItemSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # def create(self, request):
    #     breakpoint()