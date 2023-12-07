from rest_framework.serializers import ModelSerializer

from padaria.models import Item
from padaria.serializers import ProdutoDetailSerializer

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class ItemDetailSerializer(ModelSerializer):
    produto = ProdutoDetailSerializer(many=False)
    class Meta:
        model = Item
        fields = "__all__"
        depth = 2

class ItemListSerializer(ModelSerializer):
    produto = ProdutoDetailSerializer(many=False)
    class Meta:
        model = Item
        fields = "__all__"
        depth = 2