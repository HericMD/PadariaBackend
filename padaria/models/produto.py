import mimetypes
import uuid

from django.db import models
# from uploader.models import Image
# from utils.files import get_content_type

# def image_file_path(image, _):
#     extension = mimetypes.guess_extension(image.file.file.content_type)
#     if extension == ".jpe":
#         extension = ".jpg"
#     return "images/{}{}".format(image.public_id, extension or "")

from padaria.models import Categoria

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.CharField(max_length=50, null=False, blank=False)
    
    preco = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    imagem = models.ImageField(upload_to=(''), null=True, blank=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="produto", null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.preco}"

    class Meta:
        verbose_name_plural = "Produtos"
