from rest_framework.serializers import ModelSerializer

from padaria.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        depth = 1