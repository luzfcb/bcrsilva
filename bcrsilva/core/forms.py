from django import forms
from .models import Contato
from bcrsilva.core.models import Pessoa
from django.forms.models import inlineformset_factory

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'

ContatoFormSet = forms.modelformset_factory(
    Contato,
    form=ContatoForm,
    extra=2
)

ContatoInlineFormSet = forms.inlineformset_factory(
    Pessoa,
    Contato,
    extra=2,
    fields=('email', 'telefone'),
    formset=ContatoFormSet,
    min_num=0,
    max_num=4,
    can_delete=True,
    widgets = {
        'email': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insira o email',
                'style': 'margin-bottom: 1em'
            }
        ),
        'telefone': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insira o telefone',
            }
        )
    }
)
