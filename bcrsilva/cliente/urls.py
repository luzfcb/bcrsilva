from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^pessoa-juridica$', views.listar_clientesPJ, name='listar_clientesPJ'),
    url(r'^pessoa-juridica/novo/$', views.novo_clientePJ, name='novo_clientePJ'),
    url(r'^pessoa-juridica/editar/(?P<pk>\d+)/$',
        views.editar_clientePJ, name='editar_clientePJ'),
    url(r'^pessoa-juridica/excluir/(?P<pk>\d+)/$',
        views.excluir_clientePJ, name='excluir_clientePJ'),
    url(r'^pessoa-fisica$', views.listar_clientesPF, name='listar_clientesPF'),
    url(r'^pessoa-fisica/novo/$', views.novo_clientePF, name='novo_clientePF'),
    url(r'^pessoa-fisica/editar/(?P<pk>\d+)/$',
        views.editar_clientePF, name='editar_clientePF'),
    url(r'^pessoa-fisica/excluir/(?P<pk>\d+)/$',
        views.excluir_clientePF, name='excluir_clientePF'),
]
