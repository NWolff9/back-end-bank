
import decimal
from rest_framework import viewsets, status
from rest_framework.response import Response

from cadastro.api.serializers import ClienteSerializer, ClienteFotoSerializer, UsuarioSerializer, ContaSerializer, CartaoSerializer, FaturaSerializer, EmprestimoSerializer, Pagamento_emprestimoSerializer, TransacaoSerializer, ContatosSerializer, ExtratoSerializer
from cadastro.models import Cliente, Usuario, Cartao, Conta, Contatos, Emprestimo, Extrato, Fatura, Pagamento_emprestimo, Transacao

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteFotoViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteFotoSerializer

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

    def create(self, request, *args, **kwargs):
        #fazer a logica de subtrair o valor da conta do cliente conforme o pagamento da fatura
        #usuario1 = 
        return super().create(request, *args, **kwargs)

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class Pagamento_emprestimoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento_emprestimo.objects.all()
    serializer_class = Pagamento_emprestimoSerializer

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

    def create(self, request, *args, **kwargs):
        #pegar o id do cliente pois estamos passando o id_usuario
        remetente = self.request.data['remetente']
        destinatario = self.request.data['destinatario']
        usuario1 = Usuario.objects.get(fk_cliente_id=remetente)
        usuario2 = Usuario.objects.get(fk_cliente_id=destinatario)


        #verificar saldo da conta remetente
        conta_remetente = Conta.objects.get(fk_usuario=usuario1.pk)
        if conta_remetente:
            valor_transferencia = decimal.Decimal(self.request.data['valor'])
            if conta_remetente.saldo >= valor_transferencia:
                #subtrair dinheiro da conta
                novo_saldo = conta_remetente.saldo - valor_transferencia
                conta_atualizar = {'numero_conta': conta_remetente.numero_conta, 'agencia': conta_remetente.agencia, 'saldo': novo_saldo, 'fk_usuario': usuario1.pk }
                serializer_remetente = ContaSerializer(conta_remetente, conta_atualizar)
                if serializer_remetente.is_valid():
                    serializer_remetente.save()
                else:
                    print(serializer_remetente.errors)
                add_extrato_remetente = { 'operacao' : 'O', 'descritivo': 'Transferência entre contas', 'valor': valor_transferencia, 'fk_conta': conta_remetente.pk }
                serializer_extrato_rem = ExtratoSerializer(data=add_extrato_remetente)
                if serializer_extrato_rem.is_valid():
                    serializer_extrato_rem.save()
                else:
                    print(serializer_extrato_rem.errors)

                #quem vai receber o dinheiro (destinatário)
                
                conta_destinatario = Conta.objects.get(fk_usuario=usuario2.pk)
                if conta_destinatario:
                    add_saldo = conta_destinatario.saldo + valor_transferencia
                    conta_atualizar_dest = {'numero_conta': conta_destinatario.numero_conta, 'agencia': conta_destinatario.agencia, 'saldo': add_saldo, 'fk_usuario': usuario2.pk }
                    serializer_destinatario = ContaSerializer(conta_destinatario, conta_atualizar_dest)
                    if serializer_destinatario.is_valid():
                        serializer_destinatario.save()
                    else:
                        print(serializer_destinatario.errors)
                    add_extrato_destinatario = { 'operacao' : 'I', 'descritivo': 'Recebimento de transferência', 'valor': valor_transferencia, 'fk_conta': conta_destinatario.pk }
                    serializer_extrato_des = ExtratoSerializer(data=add_extrato_destinatario)
                    if serializer_extrato_des.is_valid():
                        serializer_extrato_des.save()
                return super().create(request, *args, **kwargs)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

class ContatosViewSet(viewsets.ModelViewSet):
    queryset = Contatos.objects.all()
    serializer_class = ContatosSerializer

class  ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class =  ExtratoSerializer