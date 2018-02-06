from django.contrib import admin
from .models import ItemNota, NotaEntrada

# class ItemNotaAdmin(admin.ModelAdmin):
#     list_display = [
#         'produto', 'quantidade'
#     ]
#     search_fields = ['produto']
#     list_filter = ['produto']
#
# admin.site.register(ItemNota, ItemNotaAdmin)

class ItemNotaInlineAdmin(admin.StackedInline):
    model = ItemNota

class NotaEntradaAdmin(admin.ModelAdmin):
    list_display = [
        'fornecedor', 'tipo_entrada', 'data_entrada', 'data_emissao', 'status', 'TOTAL'
    ]
    search_fields = ['fornecedor', 'data_entrada', 'status']
    list_filter = ['data_entrada', 'data_emissao', 'status', 'tipo_entrada']
    inlines = [ItemNotaInlineAdmin]

    def TOTAL(self, obj):
        total = 0
        for item in obj.itensNota.all():
            total += item.valor
        return total

    # def Total(self, obj):
    #     total = 0
    #     for item in obj.itensNota.all():
    #         total += item.produto.preco_custo * item.quantidade
    #     return total

admin.site.register(NotaEntrada, NotaEntradaAdmin)
