from django.db import models
from model_utils import FieldTracker

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', blank=True)
    preco_anterior = models.DecimalField(
        'Preço anterior', max_digits=7, decimal_places=2,
        blank=True, null=True, editable = False
    )

    preco_custo = models.DecimalField(
        'Preço de custo', max_digits=7, decimal_places=2
    )

    preco_venda = models.DecimalField(
        'Preço de venda', max_digits=7, decimal_places=2
    )
    lucro = models.DecimalField(
        'Lucro %', max_digits=5, decimal_places=2, editable=False
    )
    unidade_medida_choices = (
        ('ml', 'mililitro'),
        ('l', 'litro'),
        ('mm', 'milímetro'),
        ('cm', 'centímetro'),
        ('m', 'metro'),
        ('mg', 'miligrama'),
        ('g', 'grama'),
        ('kg', 'quilograma'),
        ('un', 'unidade'),
        ('cx', 'caixa'),
        ('pc', 'pacote'),
        ('sc', 'saco'),
        ('p', 'par')
    )
    unidade_medida = models.CharField(
        'Unidade de medida',
        max_length = 2,
        choices = unidade_medida_choices
    )

    multiplo = models.DecimalField('Múltiplo', max_digits=7, decimal_places=2)
    ncm = models.CharField('NCM', max_length=20)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria',
        related_name='produtos',
        on_delete=models.CASCADE
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    tracker = FieldTracker()

    def save(self, *args, **kwargs):
        self.lucro = (
            ((self.preco_venda - self.preco_custo) * 100) / self.preco_custo
        )
        if self.tracker.has_changed('preco_venda'):
            self.preco_anterior = self.tracker.previous('preco_venda')
            super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']
