from django.db import models
from bcrsilva.core.models import PessoaJuridica, PessoaFisica


class ClientePJ(PessoaJuridica):
    def __str__(self):
        return '%s - %s' % (self.razao_social, self.nome_fantasia)

    class Meta:
        verbose_name = 'Cliente (PJ)'
        verbose_name_plural = 'Clientes (PJ)'
        ordering = ['razao_social']


class ClientePF(PessoaFisica):
    def __str__(self):
        return '%s - %s' % (self.nome, self.apelido)

    class Meta:
        verbose_name = 'Cliente (PF)'
        verbose_name_plural = 'Clientes (PF)'
        ordering = ['nome']
