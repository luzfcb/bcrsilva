from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Categoria, Produto
from .forms import CategoriaForm, ProdutoForm

def home(request):
    atualizado_em = datetime.now()
    produtos = Produto.objects.all()
    template_name = 'produto/home.html'
    context = {
        'produtos': produtos,
        'atualizado_em': atualizado_em
    }
    return render(request, template_name, context)

def novo_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto:home')
    else:
        form = ProdutoForm()
    template_name = 'produto/editar_produto.html'
    context = {
        'form': form,
        'title': 'Registrar produto'
    }
    return render(request, template_name, context)

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto:home')
    else:
        form = ProdutoForm(instance=produto)
    template_name = 'produto/editar_produto.html'
    context = {
        'form': form,
        'title': 'Editar produto',
        'produto': produto
    }
    return render(request, template_name, context)

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == "POST":
        produto.delete()
        return redirect('produto:home')
    template_name = 'confirmar_delete.html'
    context = {
        'objeto': produto,
        'title': 'Excluir produto',
        'mensagem': 'Tem certeza que quer deletar o Produto: '
    }
    return render(request, template_name, context)

def lista_categorias(request):
    atualizado_em = datetime.now()
    categorias = Categoria.objects.all()
    template_name = 'produto/lista_categorias.html'
    context = {
        'categorias': categorias,
        'atualizado_em': atualizado_em
    }
    return render(request, template_name, context)

def detalhes_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    template_name = 'produto/detalhes_categoria.html'
    context = {
        'categoria': categoria
    }
    return render(request, template_name, context)

def nova_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto:lista_categorias')
    else:
        form = CategoriaForm()
    template_name = 'produto/editar_categoria.html'
    context = {
        'form': form,
        'title': 'Registrar categoria'
    }
    return render(request, template_name, context)

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('produto:lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    template_name = 'produto/editar_categoria.html'
    context = {
        'form': form,
        'title': 'Editar categoria',
        'categoria': categoria
    }
    return render(request, template_name, context)

def excluir_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == "POST":
        categoria.delete()
        return redirect('produto:lista_categorias')
    template_name = 'confirmar_delete.html'
    context = {
        'objeto': categoria,
        'title': 'Excluir categoria',
        'mensagem': 'Tem certeza que quer deletar a Categoria: '
    }
    return render(request, template_name, context)
