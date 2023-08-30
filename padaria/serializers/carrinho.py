from rest_framework.serializers import ModelSerializer

from padaria.models import Carrinho

class CarrinhoSerializer(ModelSerializer):
    class Meta:
        model = Carrinho
        fields = "__all__"