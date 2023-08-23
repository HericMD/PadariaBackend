from rest_framework.serializers import ModelSerializer

from uploader.serializers import ImageSerializer

from padaria.models import Produto

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1


class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "descricao", "preco", "file"]
        depth = 1
        