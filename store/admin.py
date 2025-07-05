from django.contrib import admin
from .models import Product, Order

# Registra o modelo de Produto no painel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)

# Registra o modelo de Pedido no painel
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product', 'customer_phone', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'customer_phone', 'product__name')

    # Deixa os detalhes do pedido como "somente leitura" para evitar acidentes
    readonly_fields = ('product', 'customer_name', 'customer_phone', 'customer_email', 
                       'customer_cep', 'customer_neighborhood', 'customer_address', 
                       'customer_reference', 'created_at')

    def get_fields(self, request, obj=None):
        if obj:
            return ('status', 'product', 'customer_name', 'customer_phone', 'customer_email', 
                    'customer_cep', 'customer_neighborhood', 'customer_address', 
                    'customer_reference', 'created_at')
        return super().get_fields(request, obj)