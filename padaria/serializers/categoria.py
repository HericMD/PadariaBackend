from rest_framework.serializers import ModelSerializer, CharField

from padaria.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class CategoriaDetailSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        depth = 1

class CategoriaListSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        depth = 1