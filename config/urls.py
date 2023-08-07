from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from padaria.views import CarrinhoViewSet, EnderecoViewSet, ProdutoViewSet, UsuarioViewSet

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
router.register(r"carrinho", CarrinhoViewSet)
router.register(r"endereco", EnderecoViewSet)
router.register(r"produto", ProdutoViewSet)
router.register(r"usuario", UsuarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]