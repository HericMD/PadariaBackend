from rest_framework.serializers import ModelSerializer, CharField

from padaria.models import Categoria

class CategoriaSerializer(ModelSerializer):
    # imagem = CharField(source="imagem.file", read_only=True)
    class Meta:
        model = Categoria
        fields = ["id", "descricao", "imagem"]
        # depth = 1