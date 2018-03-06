from django import forms
from .models import ItemNota, NotaEntrada

class ItemNotaForm(forms.ModelForm):
    class Meta:
        model = ItemNota
        fields = '__all__'

ItemNotaFormSet = forms.modelformset_factory(
    ItemNota,
    form=ItemNotaForm,
    extra=2
)

ItemNotaInlineFormSet = forms.inlineformset_factory(
    NotaEntrada,
    ItemNota,
    extra=2,
    fields=('produto', 'quantidade'),
    formset=ItemNotaFormSet,
    min_num=0,
    max_num=4,
    can_delete=True
    # widgets={
    #     'produto': forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Insira o email',
    #             'style': 'margin-bottom: 1em'
    #         }
    #     ),
    #     'telefone': forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Insira o telefone',
    #         }
    #     )
    # }
)

class NotaEntradaForm(forms.ModelForm):
    class Meta:
        model = NotaEntrada
        fields = [
            'data_entrada', 'data_emissao', 'status', 'fornecedor', 'descricao', 'tipo_entrada'
        ]

        widgets = {
            'data_entrada': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a data e a hora'
                }
            ),
            'data_emissao': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a data e a hora'
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecione o status'
                }
            ),
            'data_entrada': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a data e a hora'
                }
            ),
            'data_entrada': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a data e a hora'
                }
            ),
            'data_entrada': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a data e a hora'
                }
            ),
            'fornecedor': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecione o fornecedor'
                }
            ),
            'tipo_entrada': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecione a entrada'
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira a descrição',
                    'style': 'resize: none',
                    'rows': 3
                }
            )
        }
