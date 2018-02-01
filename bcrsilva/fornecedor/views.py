from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .forms import FornecedorForm
from .models import Fornecedor

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
    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedor:home')
    else:
        form = FornecedorForm()
    template_name = 'fornecedor/editar_fornecedor.html'
    context = {
        'form': form,
        'title': 'Registrar fornecedor'
    }
    return render(request, template_name, context)

def editar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == "POST":
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedor:home')
    else:
        form = FornecedorForm(instance=fornecedor)
    template_name = 'fornecedor/editar_fornecedor.html'
    context = {
        'form': form,
        'title': 'Editar fornecedor: "%s"' % (fornecedor)
    }
    return render(request, template_name, context)

def excluir_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)

    if request.method == "POST":
        fornecedor.delete()
        return redirect('fornecedor:home')
    template_name = 'confirmar_delete.html'
    context = {
        'objeto': fornecedor,
        'title': 'Excluir fornecedor',
        'mensagem': 'Tem certeza que quer deletar o Fornecedor: '
    }
    return render(request, template_name, context)
