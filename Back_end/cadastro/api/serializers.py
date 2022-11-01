from rest_framework import serializers
from cadastro.models import Cliente, Usuario, Conta, Cartao, Fatura, Emprestimo, Pagamento_emprestimo, Transacao, Contatos, Extrato
from pictures.contrib.rest_framework import PictureField

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nome','sobrenome','celular','endereco','email','cpf','foto']
    #foto = PictureField()

class ClienteFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome','sobrenome','celular','endereco','email','cpf','foto']
    foto = PictureField()

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['senha','fk_cliente']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['numero_conta','agencia','saldo','fk_usuario']

class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        fields = ['valor_fatura','data_pagamento_efetuado','data_validade','fk_cartao']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['aprovacao','valor','data','taxa_juros','parcelas_pagas','valor_com_juros','funcionarios','Justificativa','fk_cliente']

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['remetente','destinatario','valor','data']

class ContatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contatos
        fields = ['Titular','Favorito']

class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ['numero_cartao','finalidade','validade','situacao','cvv','vencimento_fatura','fk_conta']

class Pagamento_emprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento_emprestimo
        fields = ['vencimento','pagamento','valor_parcela','fk_emprestimo']

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = ['horario','opercacao','descritivo','valor','fk_conta']





