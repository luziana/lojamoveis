# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import cadastrar_cliente, cadastrar_funcionario

urlpatterns = [
    url(r'^entrar/$', login, name='entrar'),
    url(r'^sair/$', logout, {'next_page': 'entrar'}, name='sair'),
    url(r'^cadastrar_cliente/$', cadastrar_cliente, name='cadastrar_cliente'),
    url(r'^cadastrar_funcionario/$', cadastrar_funcionario, name='cadastrar_funcionario'),

]