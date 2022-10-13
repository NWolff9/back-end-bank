from django.contrib import admin
from .models import Cartao, Cliente, Contatos, Emprestimo, Extrato, Fatura, Pagamento_emprestimo, Transacao, Usuario, Conta

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Conta)
admin.site.register(Cartao)
admin.site.register(Fatura)
admin.site.register(Emprestimo)
admin.site.register(Pagamento_emprestimo)
admin.site.register(Transacao)
admin.site.register(Contatos)
admin.site.register(Extrato)
