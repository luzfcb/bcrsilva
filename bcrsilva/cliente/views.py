from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from .models import ClientePJ, ClientePF
from .forms import ClientePJForm, ClientePFForm
from bcrsilva.core.models import Contato
from bcrsilva.core.forms import ContatoInlineFormSet

def listar_clientesPJ(request):
    atualizado_em = datetime.now()
    clientes = ClientePJ.objects.all()
    template_name = 'cliente/listar_clientesPJ.html'
    context = {
        'clientes': clientes,
        'atualizado_em': atualizado_em
    }
    return render(request, template_name, context)

def novo_clientePJ(request):
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
            clientePJ = form.save(commit=False)
            clientePJ.save()
            contatos = contato_forms.save(commit=False)
            for contato in contatos:
                contato.pessoa = clientePJ
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

def editar_clientePJ(request, pk):
    clientePJ = get_object_or_404(ClientePJ, pk=pk)
    form = ClientePJForm(instance=clientePJ)
    contato_forms = ContatoInlineFormSet(
        queryset=form.instance.contatos.all()
    )

    if request.method == "POST":
        form = ClientePJForm(request.POST, instance=clientePJ)
        contato_forms = ContatoInlineFormSet(
            request.POST,
            queryset=form.instance.contatos.all()
        )
        if form.is_valid() and contato_forms.is_valid():
            form.save()
            contatos = contato_forms.save(commit=False)
            for contato in contatos:
                contato.pessoa = clientePJ
                contato.save()
            messages.success(request, 'Cliente(PJ) alterado com sucesso!')
            return redirect('cliente:listar_clientesPJ')
    template_name = 'cliente/editar_clientePJ.html'
    context = {
        'form': form,
        'formset': contato_forms,
        'title': 'Editar cliente (PJ): "%s"' % (clientePJ)
    }
    return render(request, template_name, context)

def excluir_clientePJ(request, pk):
    clientePJ = get_object_or_404(ClientePJ, pk=pk)

    if request.method == "POST":
        clientePJ.delete()
        messages.success(request, 'Cliente(PJ) excluído com sucesso!')
        return redirect('cliente:listar_clientesPJ')
    template_name = 'confirmar_delete.html'
    context = {
        'objeto': clientePJ,
        'title': 'Excluir cliente',
        'mensagem': 'Tem certeza que quer deletar o Cliente (PJ): ',
        'clientePJ': True
    }
    return render(request, template_name, context)

def listar_clientesPF(request):
    atualizado_em = datetime.now()
    clientes = ClientePF.objects.all()
    template_name = 'cliente/listar_clientesPF.html'
    context = {
        'clientes': clientes,
        'atualizado_em': atualizado_em
    }
    return render(request, template_name, context)

def novo_clientePF(request):
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
            clientePF = form.save(commit=False)
            clientePF.save()
            contatos = contato_forms.save(commit=False)
            for contato in contatos:
                contato.pessoa = clientePF
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

def editar_clientePF(request, pk):
    clientePF = get_object_or_404(ClientePF, pk=pk)
    form = ClientePFForm(instance=clientePF)
    contato_forms = ContatoInlineFormSet(
        queryset=form.instance.contatos.all()
    )

    if request.method == "POST":
        form = ClientePFForm(request.POST, instance=clientePF)
        contato_forms = ContatoInlineFormSet(
            request.POST,
            queryset=form.instance.contatos.all()
        )
        if form.is_valid() and contato_forms.is_valid():
            form.save()
            contatos = contato_forms.save(commit=False)
            for contato in contatos:
                contato.pessoa = clientePF
                contato.save()
            messages.success(request, 'Cliente(PF) alterado com sucesso!')
            return redirect('cliente:listar_clientesPF')
    template_name = 'cliente/editar_clientePF.html'
    context = {
        'form': form,
        'formset': contato_forms,
        'title': 'Editar cliente (PF): "%s"' % (clientePF)
    }
    return render(request, template_name, context)

def excluir_clientePF(request, pk):
    clientePF = get_object_or_404(ClientePF, pk=pk)

    if request.method == "POST":
        clientePF.delete()
        messages.success(request, 'Cliente(PF) excluído com sucesso!')
        return redirect('cliente:listar_clientesPF')
    template_name = 'confirmar_delete.html'
    context = {
        'objeto': clientePF,
        'title': 'Excluir cliente',
        'mensagem': 'Tem certeza que quer deletar o Cliente (PF): ',
        'clientePF': True
    }
    return render(request, template_name, context)
