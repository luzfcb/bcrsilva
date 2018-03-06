from django.db import models
from bcrsilva.fornecedor.models import Fornecedor
from bcrsilva.produto.models import Produto


class Nota(models.Model):
    data_entrada = models.DateTimeField('Entrada')
    data_emissao = models.DateTimeField('Emissão')
    total = models.DecimalField(
        'Total', max_digits=7, decimal_places=2, editable=False, default=0
    )
    status_choices = (
        ('A', 'Em aberto'),
        ('C', 'Cancelada'),
        ('P', 'Processada')
    )
    status = models.CharField(
        'Status',
        max_length=1,
        choices=status_choices,
        default='A'
    )
    criado_em = models.DateTimeField('Criada em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizada em', auto_now=True)


class NotaEntrada(Nota):
    fornecedor = models.ForeignKey(Fornecedor, verbose_name='Fornecedor',
                                   related_name='entradas',
                                   on_delete=models.CASCADE
                                   )
    descricao = models.TextField('Descrição', blank=True, null=True)
    tipo_entrada_choices = (
        ('C', 'Compra'),
        ('G', 'Garantia')
    )
    tipo_entrada = models.CharField(
        'Tipo de entrada',
        max_length=1,
        choices=tipo_entrada_choices
    )

    def __str__(self):
        return "%s - %s" % (self.fornecedor, self.data_entrada)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['data_entrada']


class ItemNota(models.Model):
    produto = models.ForeignKey(Produto, verbose_name='Produto',
                                related_name='itensNota',
                                on_delete=models.CASCADE
                                )
    nota = models.ForeignKey(Nota, verbose_name='Nota',
                             related_name='itensNota',
                             on_delete=models.CASCADE
                             )
    quantidade = models.IntegerField('Quantidade')
    valor = models.DecimalField(
        'Valor', max_digits=7, decimal_places=2, editable=False, default=0
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    # def save(self, *args, **kwargs):
    #     self.valor = self.produto.preco_custo * self.quantidade
    #     super().save(*args, **kwargs)
