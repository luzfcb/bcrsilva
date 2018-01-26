from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^categoria/$', views.lista_categorias, name="lista_categorias"),
    url(r'^categoria/(?P<pk>\d+)/$', views.detalhes_categoria, name='detalhes_categoria'),
    url(r'^categoria/nova/$', views.nova_categoria, name='nova_categoria'),
    url(r'^categoria/editar/(?P<pk>\d+)/$', views.editar_categoria, name='editar_categoria'),
    url(r'^categoria/excluir/(?P<pk>\d+)/$', views.excluir_categoria, name='excluir_categoria'),
]
