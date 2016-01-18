# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.IntegerField(default=0)),
                ('bairro', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('cep', models.IntegerField()),
                ('estado', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpj', models.CharField(max_length=200)),
                ('inscricao_estadual', models.IntegerField()),
                ('inscricao_municipal', models.IntegerField()),
                ('razao', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('representante', models.CharField(max_length=200)),
                ('telefone_representante', models.IntegerField()),
                ('observacoes', models.TextField(max_length=500)),
                ('endereco', models.ForeignKey(to='cadastros.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField()),
                ('hora_entrada', models.DateTimeField()),
                ('hora_saida', models.DateTimeField()),
                ('comissao', models.FloatField()),
                ('desconto', models.FloatField()),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.IntegerField()),
                ('desativado', models.BooleanField()),
                ('cargo', models.ForeignKey(to='cadastros.Cargo')),
                ('endereco', models.ForeignKey(to='cadastros.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Mercadoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=200)),
                ('referencia', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=200)),
                ('valor_venda', models.FloatField(default=0)),
                ('desconto', models.FloatField(default=0)),
            ],
        ),
    ]
