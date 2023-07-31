from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from padaria.views import CarrinhoViewSet, EnderecoViewSet, ProdutoViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r"carrinho", CarrinhoViewSet)
router.register(r"endereco", EnderecoViewSet)
router.register(r"produto", ProdutoViewSet)
router.register(r"usuario", UsuarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]