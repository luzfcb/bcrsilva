from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from .models import ClientePJ, ClientePF
from .forms import ClientePJForm, ClientePFForm
from bcrsilva.core.models import Contato
from bcrsilva.core.forms import ContatoInlineFormSet


def listar_clientes_pj(request):
    atualizado_em = datetime.now()
    clientes = ClientePJ.objects.all()
    template_name = 'cliente/listar_clientesPJ.html'
    context = {
        'clientes': clientes,
        'atualizado_em': atualizado_em
    }
    return render(request, template_name, context)


def novo_cliente_pj(request):
    form = ClientePJForm()
    contato_forms = ContatoInlineFormSet(
        queryset=Contato.objects.none()
    )

    if request.method == "POST":
        form = ClientePJForm(request.POST)
        contato_forms = ContatoInlineFormSet(
            request.POST,
            queryset=Contato.objects.none()
        )
        if form.is_valid() and contato_forms.is_valid():
            cliente_pj_obj = form.save(commit=False)
            cliente_pj_obj.save()
            contatos = contato_forms.save(commit=False)
            for contato in contatos:
                contato.pessoa = cliente_pj_obj
                contato.save()
            messages.success(request, 'Cliente(PJ) salvo com sucesso!')
            return redirect('cliente:listar_clientesPJ')
    template_name = 'cliente/editar_clientePJ.html'
    context = {
        'form': form,
        'formset': contato_forms,
        'title': 'Registrar cliente (PJ)'
    }
    return render(request, template_name, context)


def editar_cliente_pj(request, pk):
    cliente_pj_obj = get_object_or_404(ClientePJ, pk=pk)
    form = ClientePJForm(instance=cliente_pj_obj)
    contato_forms = ContatoInlineFormSet(
        queryset=form.instance.contatos.all()
    )

    if request.method == "POST":
        form = ClientePJForm(request.POST, instance=cliente_pj_obj)
        contato_forms = ContatoInlineFormSet(
            request.POST,
            queryset=form.instance.contatos.all()
        )
        if form.is_valid() and contato_forms.is_valid():
            form.save()
            contatos = contato_forms.save(commit=False)
            for contato in contatos:
                contato.pessoa = cliente_pj_obj
                contato.save()
            messages.success(request, 'Cliente(PJ) alterado com sucesso!')
            return redirect('cliente:listar_clientesPJ')
    template_name = 'cliente/editar_clientePJ.html'
    context = {
        'form': form,
        'formset': contato_forms,
        'title': 'Editar cliente (PJ): "%s"' % (cliente_pj_obj)
    }
    return render(request, template_name, context)


def excluir_cliente_pj(request, pk):
    cliente_pj_obj = get_object_or_404(ClientePJ, pk=pk)

    if request.method == "POST":
        cliente_pj_obj.delete()
        messages.success(request, 'Cliente(PJ) excluído com sucesso!')
        return redirect('cliente:listar_clientesPJ')
    template_name = 'confirmar_delete.html'
    context = {
        'objeto': cliente_pj_obj,
        'title': 'Excluir cliente',
        'mensagem': 'Tem certeza que quer deletar o Cliente (PJ): ',
        'clientePJ': True
    }
    return render(request, template_name, context)


def listar_clientes_pf(request):
    atualizado_em = datetime.now()
    clientes = ClientePF.objects.all()
    template_name = 'cliente/listar_clientesPF.html'
    context = {
        'clientes': clientes,
        'atualizado_em': atualizado_em
    }
    return render(request, template_name, context)


def novo_cliente_pf(request):
    form = ClientePFForm()
    contato_forms = ContatoInlineFormSet(
        queryset=Contato.objects.none()
    )

    if request.method == "POST":
        form = ClientePFForm(request.POST)
        contato_forms = ContatoInlineFormSet(
            request.POST,
            queryset=Contato.objects.none()
        )
        if form.is_valid() and contato_forms.is_valid():
            cliente_pf_obj = form.save(commit=False)
            cliente_pf_obj.save()
            contatos = contato_forms.save(commit=False)
            for contato in contatos:
                contato.pessoa = cliente_pf_obj
                contato.save()
            messages.success(request, 'Cliente(PF) salvo com sucesso!')
            return redirect('cliente:listar_clientesPF')
    template_name = 'cliente/editar_clientePF.html'
    context = {
        'form': form,
        'formset': contato_forms,
        'title': 'Registrar cliente (PF)'
    }
    return render(request, template_name, context)


def editar_cliente_pf(request, pk):
    cliente_pf_obj = get_object_or_404(ClientePF, pk=pk)
    form = ClientePFForm(instance=cliente_pf_obj)
    contato_forms = ContatoInlineFormSet(
        queryset=form.instance.contatos.all()
    )

    if request.method == "POST":
        form = ClientePFForm(request.POST, instance=cliente_pf_obj)
        contato_forms = ContatoInlineFormSet(
            request.POST,
            queryset=form.instance.contatos.all()
        )
        if form.is_valid() and contato_forms.is_valid():
            form.save()
            contatos = contato_forms.save(commit=False)
            for contato in contatos:
                contato.pessoa = cliente_pf_obj
                contato.save()
            messages.success(request, 'Cliente(PF) alterado com sucesso!')
            return redirect('cliente:listar_clientesPF')
    template_name = 'cliente/editar_clientePF.html'
    context = {
        'form': form,
        'formset': contato_forms,
        'title': 'Editar cliente (PF): "%s"' % (cliente_pf_obj)
    }
    return render(request, template_name, context)


def excluir_cliente_pf(request, pk):
    cliente_pf_obj = get_object_or_404(ClientePF, pk=pk)

    if request.method == "POST":
        cliente_pf_obj.delete()
        messages.success(request, 'Cliente(PF) excluído com sucesso!')
        return redirect('cliente:listar_clientesPF')
    template_name = 'confirmar_delete.html'
    context = {
        'objeto': cliente_pf_obj,
        'title': 'Excluir cliente',
        'mensagem': 'Tem certeza que quer deletar o Cliente (PF): ',
        'clientePF': True
    }
    return render(request, template_name, context)
