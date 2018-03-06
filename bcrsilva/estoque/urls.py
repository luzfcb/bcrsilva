from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^entrada/$', views.home, name='home'),
    url(r'^entrada/nova/$', views.nova_notaEntrada, name='nova_notaEntrada'),
    url(r'^entrada/editar/(?P<pk>\d+)/$', views.editar_notaEntrada, name='editar_notaEntrada'),
    url(r'^entrada/excluir/(?P<pk>\d+)/$', views.excluir_notaEntrada,
        name='excluir_notaEntrada'),
]
