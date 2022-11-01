from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from pictures.conf import get_settings
from django.conf.urls.static import static
from django.conf import settings
from cadastro.api.viewsets import ClienteViewSet, ClienteFotoViewSet, UsuarioViewSet, ContaViewSet, CartaoViewSet, FaturaViewSet, EmprestimoViewSet, Pagamento_emprestimoViewSet, TransacaoViewSet, ContatosViewSet, ExtratoViewSet

route = routers.DefaultRouter()
route.register(r'cliente', ClienteViewSet, basename="Cliente")
route.register(r'cliente-foto', ClienteFotoViewSet, basename="Cliente-Foto")
route.register(r'usuario', UsuarioViewSet, basename="Usuario")
route.register(r'conta', ContaViewSet, basename="Conta")
route.register(r'cartao', CartaoViewSet, basename="Cartao")
route.register(r'fatura', FaturaViewSet, basename="Fatura")
route.register(r'emprestimo', EmprestimoViewSet, basename="Emprestimo")
route.register(r'pagamento_emprestimo', Pagamento_emprestimoViewSet, basename="Pagamento_emprestimo")
route.register(r'transacao', TransacaoViewSet, basename="Transacao")
route.register(r'contatos',ContatosViewSet, basename="Contatos")
route.register(r'extrato', ExtratoViewSet, basename="Extrato")

urlpatterns = [
     path('', include(route.urls)),
     path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if get_settings().USE_PLACEHOLDERS:
#     urlpatterns += [
#         path("galeria/", include("pictures.urls")),
#     ]
