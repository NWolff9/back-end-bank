from rest_framework import viewsets
from Back_end.cadastro.models import Cartao, Conta, Contatos, Emprestimo, Extrato, Fatura, Pagamento_emprestimo, Transacao
from cadastro.api.serializers import ClienteSerializer, UsuarioSerializer, ContaSerializer, CartaoSerializer, FaturaSerializer, EmprestimoSerializer, Pagamento_emprestimoSerializer, TransacaoSerializer, ContatosSerializer, ExtratoSerializer
from cadastro.models import Cliente, Usuario

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

class FaturaViewSet(viewsets.ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class Pagamento_emprestimoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento_emprestimo.objects.all()
    serializer_class = Pagamento_emprestimoSerializer

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

class ContatosViewSet(viewsets.ModelViewSet):
    queryset = Contatos.objects.all()
    serializer_class = ContatosSerializer

class  ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class =  ExtratoSerializer