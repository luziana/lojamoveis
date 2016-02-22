# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import cadastrar_cliente, cadastrar_funcionario, cadastrar_mercadoria, cadastrar_fornecedor, \
    cadastrar_compra, cadastrar_conta_pagar, cadastrar_conta_receber, list_clientes, list_funcionarios

urlpatterns = [
    url(r'^entrar/$', login, name='entrar'),
    url(r'^sair/$', logout, {'next_page': 'entrar'}, name='sair'),
    url(r'^cadastrar_cliente/$', cadastrar_cliente, name='cadastrar_cliente'),
    url(r'^list_clientes/$', list_clientes, name='list_clientes'),
    url(r'^cadastrar_funcionario/$', cadastrar_funcionario, name='cadastrar_funcionario'),
     url(r'^list_funcionarios/$', list_funcionarios, name='list_funcionarios'),
    url(r'^cadastrar_mercadoria/$', cadastrar_mercadoria, name='cadastrar_mercadoria'),
    url(r'^cadastrar_fornecedor/$', cadastrar_fornecedor, name='cadastrar_fornecedor'),
    url(r'^cadastrar_compra/$', cadastrar_compra, name='cadastrar_compra'),
    url(r'^cadastrar_conta_pagar/$', cadastrar_conta_pagar, name='cadastrar_conta_pagar'),
    url(r'^cadastrar_conta_receber/$', cadastrar_conta_receber, name='cadastrar_conta_receber'),

]