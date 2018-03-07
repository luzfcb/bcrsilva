from django import forms
from .models import ClientePJ, ClientePF


class ClientePJForm(forms.ModelForm):
    class Meta:
        model = ClientePJ
        fields = [
            'razao_social', 'nome_fantasia', 'cnpj', 'inscricao_estadual',
            'cep', 'endereco', 'numero', 'bairro', 'cidade', 'uf'
        ]

        widgets = {
            'razao_social': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a Razão Social'
                }
            ),
            'nome_fantasia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o Nome Fantasia'
                }
            ),
            'cnpj': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o CNPJ'
                }
            ),
            'inscricao_estadual': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a Inscrição Estadual'
                }
            ),
            'cep': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira'
                }
            ),
            'endereco': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o endereço',
                    'style': 'resize: none',
                    'rows': 1
                }
            ),
            'numero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira'
                }
            ),
            'bairro': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o bairro'
                }
            ),
            'cidade': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a cidade'
                }
            ),
            'uf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira'
                }
            )
        }


class ClientePFForm(forms.ModelForm):
    class Meta:
        model = ClientePF
        fields = [
            'nome', 'apelido', 'cpf', 'rg', 'data_nascimento',
            'cep', 'endereco', 'numero', 'bairro', 'cidade', 'uf'
        ]

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o nome'
                }
            ),
            'apelido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o apelido'
                }
            ),
            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o CPF'
                }
            ),
            'rg': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o RG'
                }
            ),
            'data_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a data'
                }
            ),
            'cep': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira'
                }
            ),
            'endereco': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o endereço',
                    'style': 'resize: none',
                    'rows': 1
                }
            ),
            'numero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira'
                }
            ),
            'bairro': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o bairro'
                }
            ),
            'cidade': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a cidade'
                }
            ),
            'uf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira'
                }
            )
        }
