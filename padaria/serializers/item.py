from rest_framework.serializers import ModelSerializer

from padaria.models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class ItemDetailSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        depth = 2

class ItemListSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        depth = 2