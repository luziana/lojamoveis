from django.db import models


class Cargo(models.Model):
    nome = models.CharField(max_length=200)


class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    cep = models.IntegerField()
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)


class Funcionario(models.Model):
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    hora_entrada = models.DateTimeField()
    hora_saida = models.DateTimeField()
    comissao = models.FloatField()
    desconto = models.FloatField()
    nome = models.CharField(max_length=200)
    telefone = models.IntegerField()
    endereco = models.ForeignKey('Endereco')
    cargo = models.ForeignKey('Cargo')
    desativado = models.BooleanField()


class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=200)
    inscricao_estadual = models.IntegerField()
    inscricao_municipal = models.IntegerField()
    razao = models.CharField(max_length=300)
    endereco = models.ForeignKey('Endereco')
    email = models.EmailField()
    representante = models.CharField(max_length=200)
    telefone_representante = models.IntegerField()
    observacoes = models.TextField(max_length=500)


class Mercadoria(models.Model):
    codigo = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)
    codigo_nfe = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    valor_venda = models.FloatField(default=0)
    desconto = models.FloatField(default=0)
    icms_compra = models.IntegerField()
    icms_sub = models.IntegerField()
    ipi = models.IntegerField()
    frete = models.IntegerField()
    embalagem = models.IntegerField()
    custo_fixo = models.IntegerField()
