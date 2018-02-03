from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from .models import Fornecedor
from .forms import FornecedorForm
from bcrsilva.core.models import Contato
from bcrsilva.core.forms import ContatoInlineFormSet

def home(request):
    atualizado_em = datetime.now()
    fornecedores = Fornecedor.objects.all()
    template_name = 'fornecedor/home.html'
    context = {
        'fornecedores': fornecedores,
        'atualizado_em': atualizado_em
    }
    return render(request, template_name, context)

def novo_fornecedor(request):
    form = FornecedorForm()
    contato_forms = ContatoInlineFormSet(
        queryset=Contato.objects.none()
    )

    if request.method == "POST":
        form = FornecedorForm(request.POST)
        contato_forms = ContatoInlineFormSet(
            request.POST,
            queryset=Contato.objects.none()
        )
        if form.is_valid() and contato_forms.is_valid():
            fornecedor = form.save(commit=False)
            fornecedor.save()
            contatos = contato_forms.save(commit=False)
            for contato in contatos:
                contato.pessoa = fornecedor
                contato.save()
            messages.success(request, 'Fornecedor salvo com sucesso!')
            return redirect('fornecedor:home')
    template_name = 'fornecedor/editar_fornecedor.html'
    context = {
        'form': form,
        'formset': contato_forms,
        'title': 'Registrar fornecedor'
    }
    return render(request, template_name, context)

def editar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    form = FornecedorForm(instance=fornecedor)
    contato_forms = ContatoInlineFormSet(
        queryset=form.instance.contatos.all()
    )

    if request.method == "POST":
        form = FornecedorForm(request.POST, instance=fornecedor)
        contato_forms = ContatoInlineFormSet(
            request.POST,
            queryset=form.instance.contatos.all()
        )
        if form.is_valid() and contato_forms.is_valid():
            form.save()
            contatos = contato_forms.save(commit=False)
            for contato in contatos:
                contato.pessoa = fornecedor
                contato.save()
            messages.success(request, 'Fornecedor alterado com sucesso!')
            return redirect('fornecedor:home')
    template_name = 'fornecedor/editar_fornecedor.html'
    context = {
        'form': form,
        'formset': contato_forms,
        'title': 'Editar fornecedor: "%s"' % (fornecedor)
    }
    return render(request, template_name, context)

def excluir_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)

    if request.method == "POST":
        fornecedor.delete()
        messages.success(request, 'Fornecedor excluído com sucesso!')
        return redirect('fornecedor:home')
    template_name = 'confirmar_delete.html'
    context = {
        'objeto': fornecedor,
        'title': 'Excluir fornecedor',
        'mensagem': 'Tem certeza que quer deletar o Fornecedor: ',
        'fornecedor': True
    }
    return render(request, template_name, context)
