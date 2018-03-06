from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import NotaEntrada, ItemNota
from .forms import NotaEntradaForm, ItemNotaInlineFormSet
from django.contrib import messages

def home(request):
    atualizado_em = datetime.now()
    notasEntrada = NotaEntrada.objects.all()
    template_name = 'estoque/home.html'
    context = {
        'notasEntrada': notasEntrada,
        'atualizado_em': atualizado_em
    }
    return render(request, template_name, context)

def nova_notaEntrada(request):
    form = NotaEntradaForm()
    itensNota_forms = ItemNotaInlineFormSet(
        queryset=ItemNota.objects.none()
    )

    if request.method == "POST":
        form = NotaEntradaForm(request.POST)
        itensNota_forms = ItemNotaInlineFormSet(
            request.POST,
            queryset=ItemNota.objects.none()
        )
        if form.is_valid() and itensNota_forms.is_valid():
            notaEntrada = form.save(commit=False)
            notaEntrada.save()
            totalNota = 0
            itensNota = itensNota_forms.save(commit=False)
            for item in itensNota:
                total = item.produto.preco_custo * item.quantidade
                totalNota += total
                item.valor = total
                item.nota = notaEntrada
                item.save()
            notaEntrada.total = totalNota
            notaEntrada.save()
            messages.success(request, 'Nota (Entrada) salva com sucesso!')
            return redirect('estoque:home')
    template_name = 'estoque/editar_notaEntrada.html'
    context = {
        'form': form,
        'formset': itensNota_forms,
        'title': 'Registrar entrada'
    }
    return render(request, template_name, context)

def editar_notaEntrada(request, pk):
    notaEntrada = get_object_or_404(NotaEntrada, pk=pk)
    form = NotaEntradaForm(instance=notaEntrada)
    itensNota_forms = ItemNotaInlineFormSet(
        queryset=form.instance.itensNota.all()
    )

    if request.method == "POST":
        form = NotaEntradaForm(request.POST, instance=notaEntrada)
        itensNota_forms = ItemNotaInlineFormSet(
            request.POST,
            queryset=form.instance.itensNota.all()
        )
        if form.is_valid() and itensNota_forms.is_valid():
            nota = form.save(commit=False)
            nota.save()
            instances = itensNota_forms.save(commit=False)
            for obj in instances:
                obj.nota = notaEntrada
                obj.save()
            for obj in itensNota_forms.deleted_objects:
                obj.delete()
            messages.success(request, 'Nota(Entrada) alterada com sucesso!')
            return redirect('estoque:home')
    template_name = 'estoque/editar_notaEntrada.html'
    context = {
        'form': form,
        'formset': itensNota_forms,
        'title': 'Editar entrada: "%s"' % (notaEntrada)
    }
    return render(request, template_name, context)

def excluir_notaEntrada(request, pk):
    notaEntrada = get_object_or_404(NotaEntrada, pk=pk)

    if request.method == "POST":
        notaEntrada.delete()
        messages.success(request, 'Nota(Entrada) excluída com sucesso!')
        return redirect('estoque:home')
    template_name = 'confirmar_delete.html'
    context = {
        'objeto': notaEntrada,
        'title': 'Excluir entrada',
        'mensagem': 'Tem certeza que quer deletar a Nota (Entrada): ',
        'notaEntrada': True
    }
    return render(request, template_name, context)
