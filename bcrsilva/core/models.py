from django.db import models

class Pessoa(models.Model):
    cep = models.CharField('CEP', max_length=8)
    endereco = models.TextField('Endereço')
    numero = models.IntegerField('Número/Lote')
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    uf = models.CharField('UF', max_length=2)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

class PessoaFisica(Pessoa):
    nome = models.CharField('Nome', max_length=100)
    apelido = models.CharField('Apelido', max_length=30, blank=True, null=True)
    rg = models.CharField('RG', max_length=20)
    cpf = models.CharField('CPF', max_length=11)
    data_nascimento = models.DateField('Data de nascimento')

class PessoaJuridica(Pessoa):
    razao_social = models.CharField('Razão Social', max_length=100)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=30, blank=True, null=True)
    cnpj = models.CharField('CNPJ', max_length=14)
    inscricao_estadual = models.CharField('Inscrição Estadual', max_length=20)

class Contato(models.Model):
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=11)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    pessoa = models.ForeignKey(Pessoa, verbose_name='Pessoa',
        related_name='contatos',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s - %s' % (self.email, self.telefone)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['email']
