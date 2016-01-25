from django.shortcuts import render, redirect
from .forms import ClienteForm

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