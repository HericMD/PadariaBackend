from rest_framework.serializers import ModelSerializer, CharField, IntegerField

from uploader.serializers import ImageSerializer

from padaria.models import Carrinho
from padaria.serializers import ItemDetailSerializer

class CarrinhoSerializer(ModelSerializer):
    class Meta:
        model = Carrinho
        fields = "__all__"

class CarrinhoDetailSerializer(ModelSerializer):
    item = ItemDetailSerializer(many=True)
    class Meta:
        model = Carrinho
        fields = "__all__"
        depth = 3

class CarrinhoListSerializer(ModelSerializer):
    item = ItemDetailSerializer(many=True)
    class Meta:
        model = Carrinho
        fields = "__all__"
        depth = 3
