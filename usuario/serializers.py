from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Usuario
from uploader.models import Image
from uploader.serializers import ImageSerializer
from padaria.models import Carrinho
from padaria.serializers import CarrinhoSerializer, EnderecoSerializer

class UsuarioSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

    carrinho = CarrinhoSerializer(required=False, read_only=False)
    endereco = EnderecoSerializer(required=False, read_only=False)

    class Meta:
        model = Usuario
        fields = "__all__"
        depth = 3