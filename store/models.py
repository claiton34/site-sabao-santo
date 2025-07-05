from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome do Produto")
    description = models.TextField(verbose_name="Descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    stock = models.PositiveIntegerField(default=0, verbose_name="Volume de Estoque")
    image = models.ImageField(upload_to='products/', verbose_name="Imagem Principal")

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('Novo', 'Novo'),
        ('Finalizado', 'Finalizado'),
    ]

    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Produto Pedido")
    customer_name = models.CharField(max_length=255, verbose_name="Nome do Cliente")
    customer_phone = models.CharField(max_length=20, verbose_name="Telefone (WhatsApp)")
    customer_email = models.EmailField(verbose_name="E-mail")
    customer_cep = models.CharField(max_length=9, verbose_name="CEP")
    customer_neighborhood = models.CharField(max_length=100, verbose_name="Bairro")
    customer_address = models.CharField(max_length=255, verbose_name="Endereço (Rua e Número)")
    customer_reference = models.TextField(blank=True, null=True, verbose_name="Referência / Complemento")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data do Pedido")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Novo', verbose_name="Status")
    
    def __str__(self):
        return f"Pedido de {self.customer_name} para {self.product.name}"