from django.db import models

# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, cpf, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not cpf:
            raise ValueError('O CPF deve ser definido')
        email = self.normalize_email(email)
        user = self.model(cpf=cpf, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, cpf, email, password=None, **extra_fields):
        return self._create_user(cpf, email, password, False, False, **extra_fields)

    def create_superuser(self, cpf, email, password, **extra_fields):
        return self._create_user(cpf, email, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    VENDEDOR = 1
    GERENTE = 2
    CAIXA = 3
    CREDIARISTA = 4
    USER_TYPE_CHOICES = (
        (VENDEDOR, u'Vendedor'),
        (GERENTE, u'Gerente'),
        (CAIXA, u'Operador Caixa'),
        (CREDIARISTA, u'Crediarista')
    )
    cpf = models.CharField(u'CPF', max_length=11, unique=True)
    email = models.EmailField(u'email', max_length=255, unique=True)
    full_name = models.CharField(u'nome completo', max_length=255, blank=True)
    date_joined = models.DateTimeField(u'data de registro', default=timezone.now)
    type = models.PositiveSmallIntegerField(u'tipo',
                                            choices=USER_TYPE_CHOICES,
                                            default=GERENTE)
    is_staff = models.BooleanField(u'staff status', default=False)
    is_active = models.BooleanField(u'ativo', default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = u'usuario'
        verbose_name_plural = u'usuarios'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def __unicode__(self):
        return self.cpf


class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    cep = models.IntegerField()
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)


class Funcionario(CustomUser):
    nome = models.CharField(max_length=200)
    rg = models.CharField(max_length=11)
    endereco = models.ForeignKey('Endereco')
    telefone = models.IntegerField()
    data_nascimento = models.DateField()
    hora_entrada = models.DateTimeField()
    hora_saida = models.DateTimeField()
    comissao = models.FloatField()
    desconto = models.FloatField()
    foto = models.ImageField()
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


class Ncm(models.Model):
    ncm = models.IntegerField()
    grupo_ncm = models.IntegerField()


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
    ncm = models.ForeignKey('Ncm')


class Cliente(models.Model):
    data_cadastro = models.DateField()
    apelido = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=16)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField()
    profissao = models.CharField(max_length=200)
    nome_pai = models.CharField(max_length=300)
    nome_mae = models.CharField(max_length=300)
    conjugue = models.CharField(max_length=300)
    endereco_cliente = models.ForeignKey('Endereco')
    empresa = models.CharField(max_length=200)
    renda = models.FloatField()
    endereco_empresa = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)
    cep = models.IntegerField()
    fones = models.IntegerField()
    email = models.EmailField()
    desativado = models.BooleanField()
    bloqueado = models.BooleanField()


class Compra(models.Model):
    fornecedor = models.ForeignKey('Fornecedor')
    data_compra = models.DateField()
    valor_compra = models.FloatField()


class Venda(models.Model):
    mercadoria = models.ForeignKey('Mercadoria')
    cliente = models.ForeignKey('Cliente')
    valor_venda = models.FloatField()
    valor_venda_bruto = models.FloatField()
    quantidade = models.IntegerField()


class Conta_a_pagar(models.Model):
    compra = models.ForeignKey('Compra')
    valor_da_conta_a_pagar = models.FloatField()
    data_vencimento = models.DateField()


class Conta_a_receber(models.Model):
    data_recebimento = models.DateField()
    valor_da_conta = models.FloatField()