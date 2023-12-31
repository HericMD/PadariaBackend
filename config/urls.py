from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router
from usuario.router import router as usuario_router

from rest_framework.routers import DefaultRouter

from padaria.views import CarrinhoViewSet, CategoriaViewSet, EnderecoViewSet, ProdutoViewSet, ItemViewSet
from uploader.views import ImageUploadViewSet
from usuario.views import UsuarioViewSet

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"carrinho", CarrinhoViewSet)
router.register(r"categoria", CategoriaViewSet)
router.register(r"endereco", EnderecoViewSet)
router.register(r"produto", ProdutoViewSet)
router.register(r"imagem", ImageUploadViewSet)
router.register(r"usuario", UsuarioViewSet)
router.register(r"item", ItemViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include(usuario_router.urls)),
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
    path("api/media/", include(uploader_router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)