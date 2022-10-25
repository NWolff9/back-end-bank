from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from cadastro.api.viewsets import ClienteViewSet, UsuarioViewSet, ContaViewSet, CartaoViewSet, FaturaViewSet, EmprestimoViewSet, Pagamento_emprestimoViewSet, TransacaoViewSet, ContatosViewSet, ExtratoViewSet

route = routers.DefaultRouter()
route.register(r'cliente', ClienteViewSet, basename="Cliente")
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
]
