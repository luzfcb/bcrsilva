from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^novo/$', views.novo_fornecedor, name='novo_fornecedor'),
    url(r'^editar/(?P<pk>\d+)/$', views.editar_fornecedor, name='editar_fornecedor'),
    url(r'^excluir/(?P<pk>\d+)/$', views.excluir_fornecedor,
        name='excluir_fornecedor'),
]
