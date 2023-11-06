from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField, SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer

from padaria.models import Produto

class ProdutoSerializer(ModelSerializer):
    cover_attachment_key = serializers.SlugRelatedField(
        source="cover",
        queryset=Image.objects.all(),       # pylint: disable=no-member
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    cover = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Produto
        fields = "__all__"

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1


class ProdutoListSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao", read_only=True)
    unidade = CharField(source="get_unidade_display", read_only=True) 
    cover_attachment_key = serializers.SlugRelatedField(
        source="cover",
        queryset=Image.objects.all(),       # pylint: disable=no-member
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    cover = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1
        