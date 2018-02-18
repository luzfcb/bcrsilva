from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pessoa-juridica$', views.listar_clientes_pj, name='listar_clientesPJ'),
    url(r'^pessoa-juridica/novo/$', views.novo_cliente_pj, name='novo_clientePJ'),
    url(r'^pessoa-juridica/editar/(?P<pk>\d+)/$',
        views.editar_cliente_pj, name='editar_clientePJ'),
    url(r'^pessoa-juridica/excluir/(?P<pk>\d+)/$',
        views.excluir_cliente_pj, name='excluir_clientePJ'),
    url(r'^pessoa-fisica$', views.listar_clientes_pf, name='listar_clientesPF'),
    url(r'^pessoa-fisica/novo/$', views.novo_cliente_pf, name='novo_clientePF'),
    url(r'^pessoa-fisica/editar/(?P<pk>\d+)/$',
        views.editar_cliente_pf, name='editar_clientePF'),
    url(r'^pessoa-fisica/excluir/(?P<pk>\d+)/$',
        views.excluir_cliente_pf, name='excluir_clientePF'),
]
