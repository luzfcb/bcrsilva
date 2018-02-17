from django.db import models
from bcrsilva.core.models import PessoaJuridica


class Fornecedor(PessoaJuridica):
    def __str__(self):
        return '%s - %s' % (self.razao_social, self.nome_fantasia)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['razao_social']
