from django.shortcuts import render, redirect
from .forms import ClienteForm, FuncionarioForm

from rest_framework.reverse import reverse_lazy


def cadastrar_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, request.FILES)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect(reverse_lazy('cadastrar_cliente'))
    else:
        cliente_form = ClienteForm()
    return render(request, 'clientes/cadastrar_cliente.html', {'cliente_form': cliente_form})


def cadastrar_funcionario(request):
    if request.method == 'POST':
        funcionario_form = FuncionarioForm(request.POST, request.FILES)
        if funcionario_form.is_valid():
            funcionario_form.save()
            return redirect(reverse_lazy('cadastrar_cliente'))
    else:
        funcionario_form = FuncionarioForm()
    return render(request, 'funcionarios/cadastrar_funcionario.html', {'funcionario_form': funcionario_form})