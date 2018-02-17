from django import forms
from .models import Categoria, Produto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira o nome'
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descreva a categoria',
                    'style': 'resize: none',
                    'rows': 5
                }
            )
        }

        # labels = {
        #     'nome': 'Nome'
        # }


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
