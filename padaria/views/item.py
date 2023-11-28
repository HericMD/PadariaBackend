from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from padaria.models import Item
from padaria.serializers import ItemSerializer, ItemListSerializer, ItemDetailSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ItemListSerializer
        elif self.action == "retrieve":
            return ItemDetailSerializer
        return ItemSerializer