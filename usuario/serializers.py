from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField

from .models import Usuario
from uploader.models import Image
from uploader.serializers import ImageSerializer
from padaria.models import Carrinho
from padaria.models import Endereco
from padaria.serializers import CarrinhoDetailSerializer, EnderecoSerializer

class UsuarioSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

    carrinho_attachment_key = SlugRelatedField(
        source="carrinho",
        queryset=Carrinho.objects.all(),
        slug_field="id",
        required=False,
        write_only=True,
    )
    carrinho = CarrinhoDetailSerializer(required=False, read_only=True)

    endereco_attachment_key = SlugRelatedField(
        source="endereco",
        queryset=Endereco.objects.all(),
        slug_field="id",
        required=False,
        write_only=True,
    )
    endereco = EnderecoSerializer(required=False, read_only=True)

    unidade = CharField(source="get_unidade_display", read_only=True)
    class Meta:
        carrinho = CarrinhoDetailSerializer(many=False)
        model = Usuario
        fields = "__all__"
        depth = 3