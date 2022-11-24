from django.db import models
from pictures.models import PictureField

class Cliente(models.Model):

    nome = models.CharField(max_length= 50)
    sobrenome = models.CharField(max_length= 50)
    celular = models.CharField(max_length= 15)
    endereco = models.CharField(max_length= 250, verbose_name = "endereço")
    email = models.EmailField(max_length = 254)
    cpf = models.CharField(max_length=11,unique=True, verbose_name = "CPF")
    foto = PictureField(
      upload_to="galeria"
    )
    def __str__(self):
        return "{}({})".format(self.nome, self.sobrenome)


class Usuario(models.Model):
    
    senha = models.CharField(max_length=255)
    # O usuario é apagado se o cliente for apagado
    fk_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, verbose_name="Cliente")
    
    def __str__(self):
        return "{}({})".format(self.fk_cliente.nome, self.fk_cliente.cpf)

class Conta(models.Model):

    numero_conta = models.CharField(max_length= 50, verbose_name ="Número da Conta")
    agencia = models.CharField(max_length= 30)
    saldo = models.DecimalField(max_digits=10, decimal_places = 2) 
    # Se apagar o Usuario a conta também vai ser apagada
    fk_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE, verbose_name ="Usuario")

    def __str__(self):
        return "{}({})".format(self.fk_usuario.fk_cliente.nome, self.numero_conta)

class Cartao(models.Model):

    TIPO_DEBITO='D'
    TIPO_CREDITO='C'
    TIPOS_CARTAO=[
        (TIPO_DEBITO,'Debito'),
        (TIPO_CREDITO,'Credito')
    ]
    numero_cartao = models.CharField(max_length= 50, verbose_name ="Número do Cartão")
    finalidade = models.CharField(max_length = 1, choices = TIPOS_CARTAO, default=TIPO_DEBITO)
    validade = models.DateField()
    situacao = models.BooleanField("Aprovado")
    cvv = models.CharField(max_length= 4,  verbose_name ="CVV")
    vencimento_fatura = models.DateField()
    # Se apagar a Conta o cartão também vai ser apagado
    fk_conta = models.ForeignKey(Conta, on_delete = models.CASCADE,  verbose_name ="Conta")

    def __str__(self):
         return "{}({})".format(self.numero_cartao, self.fk_conta.fk_usuario.fk_cliente.nome)
    
class Fatura(models.Model):

    valor_fatura =  models.DecimalField(max_digits=10, decimal_places = 2)
    data_pagamento_efetuado = models.DateField(verbose_name ="Data de efetivação do pagamento")
    data_validade = models.DateField(verbose_name ="Data de Validade")
    # para ter fatura tem que ter cartão
    fk_cartao = models.ForeignKey(Cartao,  on_delete = models.CASCADE,  verbose_name ="Cartão")

    def __str__(self):
        return "{}({})".format(self.fk_cartao.numero_cartao, self.valor_fatura)

class Emprestimo(models.Model):

    FUNCIONARIO_1='L'
    FUNCIONARIO_2='B'
    FUNCIONARIO_3='I'
    FUNCIONARIOS=[
        (FUNCIONARIO_1,'Larissa'),
        (FUNCIONARIO_2,'Brian'),
        (FUNCIONARIO_3,'Icaro')
    ]

    aprovacao = models.BooleanField()
    valor = models.DecimalField(max_digits=10, decimal_places = 2) 
    data = models.DateField()
    taxa_juros = models.DecimalField(max_digits=10, decimal_places = 2, verbose_name = 'Taxa de juros')
    parcelas_pagas = models.IntegerField( verbose_name = 'Parcelas pagas')
    valor_com_juros = models.DecimalField(max_digits=10, decimal_places = 2, verbose_name = 'Valor com juros')
    funcionarios = models.CharField(max_length = 1, choices = FUNCIONARIOS, default=FUNCIONARIO_1)
    Justificativa = models.CharField(max_length=255)
    fk_cliente = models.ForeignKey(Cliente,  on_delete = models.CASCADE,  verbose_name ="Cliente")

    def __str__(self):
        return "{}({})".format(self.fk_cliente.nome, self.aprovacao)


class Pagamento_emprestimo(models.Model):
    
    vencimento =  models.DateField()
    pagamento = models.DateField()
    valor_parcela = models.DecimalField(max_digits=10, decimal_places = 2,verbose_name = "Valor da parcela" ) 
    fk_emprestimo = models.ForeignKey(Emprestimo, on_delete = models.CASCADE, verbose_name = "Aprovação")

    def __str__(self):
        return "{}({})".format(self.fk_emprestimo.fk_cliente.nome, self.pagamento)

class Transacao(models.Model):
    #Quando o cliente ser apagado o historico de transação continua intacto
    remetente = models.ForeignKey(Cliente, on_delete = models.PROTECT, related_name = 'remetente')
    destinatario = models.ForeignKey(Cliente, on_delete = models.PROTECT, related_name = 'destinatario')
    valor = models.DecimalField(max_digits=10, decimal_places = 2) 
    data = models.DateField() 

    def __str__(self):
        return "{}({})".format(self.valor, self.remetente.nome)


class Contatos(models.Model):
    titular = models.ForeignKey(Cliente, on_delete = models.CASCADE, related_name = 'titular')
    favorito = models.ForeignKey(Cliente, on_delete = models.CASCADE, related_name = 'favorito')
    def __str__(self):
        return str(self.titular)
   
 

class Extrato(models.Model):
    ENTRADA='I'
    SAIDA='O'
    EXTRATOS=[
        (ENTRADA,'Entrada'),
        (SAIDA,'Saida'),
    ]

    horario = models.DateTimeField(auto_now_add=True)
    operacao = models.CharField(max_length = 1, choices = EXTRATOS, default=ENTRADA)
    descritivo = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places = 2) 
    fk_conta = models.ForeignKey(Conta, on_delete = models.CASCADE,  verbose_name ="Conta")

    def __str__(self):
        return str(self.fk_conta.fk_usuario.fk_cliente.nome)
