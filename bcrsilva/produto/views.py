from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm

def home(request):
    context = {}
    return render(request, 'produto/home.html', context)

def lista_categorias(request):
    categorias = Categoria.objects.all()
    template_name = 'produto/lista_categorias.html'
    context = {
        'categorias': categorias
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
        'form': form
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
        'form': form
    }
    return render(request, template_name, context)

def excluir_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == "POST":
        categoria.delete()
        return redirect('produto:lista_categorias')
    template_name = 'produto/confirmar_excluir_categoria.html'
    context = {
        'categoria': categoria
    }
    return render(request, template_name, context)
