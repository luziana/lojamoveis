from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from .models import Cliente, Funcionario
from .forms import ClienteForm, CompraForm, Conta_pagarForm, Conta_receberForm, FornecedorForm, FuncionarioForm, \
    MercadoriaForm
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


def list_clientes(request):

    clientes = Cliente.objects.all()

    paginator = Paginator(clientes, 10)

    # is_paged = False
    page = request.GET.get('page')

    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)

        # is_paged = paginator.num_pages > 1

    context = RequestContext(
        request, {
            'clientes': clientes
        }
    )

    return render_to_response('clientes/list.html', context)


def cadastrar_compra(request):
    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        if compra_form.is_valid():
            compra_form.save()
            return redirect(reverse_lazy('cadastrar_compra'))
    else:
        compra_form = CompraForm()
    return render(request, 'compras/cadastrar_compra.html', {'compra_form': compra_form})



def cadastrar_conta_pagar(request):
    if request.method == 'POST':
        conta_pagar_form = Conta_pagarForm(request.POST)
        if conta_pagar_form.is_valid():
            conta_pagar_form.save()
            return redirect(reverse_lazy('cadastrar_conta_pagar'))
    else:
        conta_pagar_form = Conta_pagarForm()
    return render(request, 'conta_pagar/cadastrar_conta_pagar.html', {'conta_pagar_form': conta_pagar_form})


def cadastrar_conta_receber(request):
    if request.method == 'POST':
        conta_receber_form = Conta_receberForm(request.POST)
        if conta_receber_form.is_valid():
            conta_receber_form.save()
            return redirect(reverse_lazy('cadastrar_conta_receber'))
    else:
        conta_receber_form = Conta_receberForm()
    return render(request, 'conta_receber/cadastrar_conta_receber.html', {'conta_receber_form': conta_receber_form})


def cadastrar_fornecedor(request):
    if request.method == 'POST':
        fornecedor_form = FornecedorForm(request.POST)
        if fornecedor_form.is_valid():
            fornecedor_form.save()
            return redirect(reverse_lazy('cadastrar_fornecedor'))
    else:
        fornecedor_form = FornecedorForm()
    return render(request, 'fornecedores/cadastrar_fornecedor.html', {'fornecedor_form': fornecedor_form})


def cadastrar_funcionario(request):
    if request.method == 'POST':
        funcionario_form = FuncionarioForm(request.POST, request.FILES)
        if funcionario_form.is_valid():
            funcionario_form.save()
            return redirect(reverse_lazy('cadastrar_funcionario'))
    else:
        funcionario_form = FuncionarioForm()
    return render(request, 'funcionarios/cadastrar_funcionario.html', {'funcionario_form': funcionario_form})


def list_funcionarios(request):

    funcionarios = Funcionario.objects.all()

    paginator = Paginator(funcionarios, 10)

    # is_paged = False
    page = request.GET.get('page')

    try:
        funcionarios = paginator.page(page)
    except PageNotAnInteger:
        funcionarios = paginator.page(1)
    except EmptyPage:
        funcionarios = paginator.page(paginator.num_pages)

        # is_paged = paginator.num_pages > 1

    context = RequestContext(
        request, {
            'funcionarios': funcionarios
        }
    )

    return render_to_response('funcionarios/list.html', context)


def cadastrar_mercadoria(request):
    if request.method == 'POST':
        mercadoria_form = MercadoriaForm(request.POST)
        if mercadoria_form.is_valid():
            mercadoria_form.save()
            return redirect(reverse_lazy('cadastrar_mercadoria'))
    else:
        mercadoria_form = MercadoriaForm()
    return render(request, 'mercadorias/cadastrar_mercadoria.html', {'mercadoria_form': mercadoria_form})