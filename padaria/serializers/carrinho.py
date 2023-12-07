from rest_framework.serializers import ModelSerializer, CharField, IntegerField

from uploader.serializers import ImageSerializer

from padaria.models import Carrinho

class CarrinhoSerializer(ModelSerializer):
    class Meta:
        model = Carrinho
        fields = "__all__"
        # depth = 1

class CarrinhoDetailSerializer(ModelSerializer):
    unidade = CharField(source="get_unidade_display", read_only=True)
    class Meta:
        model = Carrinho
        fields = "__all__"
        # fields = ["id", "unidade"]
        depth = 3

class CarrinhoListSerializer(ModelSerializer):
    class Meta:
        model = Carrinho
        fields = "__all__"
        depth = 3
