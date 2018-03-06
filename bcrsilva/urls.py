from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('bcrsilva.core.urls', namespace="core")),
    url(r'^cliente/', include('bcrsilva.cliente.urls', namespace="cliente")),
    url(r'^produto/', include('bcrsilva.produto.urls', namespace="produto")),
    url(r'^fornecedor/', include('bcrsilva.fornecedor.urls', namespace="fornecedor")),
    url(r'^estoque/', include('bcrsilva.estoque.urls', namespace="estoque")),
    url(r'^admin/', include(admin.site.urls)),
]
