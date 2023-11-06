from rest_framework.serializers import ModelSerializer, CharField, IntegerField

from uploader.serializers import ImageSerializer

from padaria.models import Carrinho

class CarrinhoSerializer(ModelSerializer):
    class Meta:
        model = Carrinho
        fields = "__all__"
        # depth = 2

class CarrinhoDetailSerializer(ModelSerializer):
    class Meta:
        model = Carrinho
        fields = "__all__"
        # depth = 2

class CarrinhoListSerializer(ModelSerializer):
    complemento = CharField(source="endereco.complemento", read_only=True)
    numero = IntegerField(source="endereco.numero", read_only=True)
    cep = IntegerField(source="endereco.cep", read_only=True)
    class Meta:
        model = Carrinho
        fields = ["id", "cep", "numero", "complemento", "item"]
        # depth = 2
