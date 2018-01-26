from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('bcrsilva.core.urls', namespace="core")),
    url(r'^produto/', include('bcrsilva.produto.urls', namespace="produto")),
    url(r'^admin/', include(admin.site.urls)),
]
