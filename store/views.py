from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction
from .models import Product, Order

# Página Inicial - Lista de Produtos
def product_list(request):
    products = Product.objects.filter(stock__gt=0) # Mostra apenas produtos com estoque
    return render(request, 'store/product_list.html', {'products': products})

# Página de Detalhes do Produto
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

# Página do Formulário de Pedido
def order_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        # Pega os dados do formulário
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        cep = request.POST.get('cep')
        neighborhood = request.POST.get('neighborhood')
        address = request.POST.get('address')
        reference = request.POST.get('reference')
        
        # Validação simples
        if not all([name, phone, email, cep, neighborhood, address]):
            # Você pode adicionar uma mensagem de erro aqui se quiser
            return render(request, 'store/order_form.html', {'product': product, 'error': 'Por favor, preencha todos os campos obrigatórios.'})

        try:
            # Garante que a criação do pedido e a baixa do estoque aconteçam juntas
            with transaction.atomic():
                # Cria e salva o pedido
                order = Order.objects.create(
                    product=product,
                    customer_name=name,
                    customer_phone=phone,
                    customer_email=email,
                    customer_cep=cep,
                    customer_neighborhood=neighborhood,
                    customer_address=address,
                    customer_reference=reference,
                )
                
                # Dá baixa no estoque
                product.stock -= 1
                product.save()

            # Prepara e envia o e-mail
            subject = f'Novo Pedido Recebido: {product.name}'
            message = f"""
            Você recebeu um novo pedido!

            Produto: {product.name}
            Preço: R$ {product.price}
            -------------------------------------
            DADOS DO CLIENTE:
            Nome: {name}
            Telefone/WhatsApp: {phone}
            E-mail: {email}
            -------------------------------------
            ENDEREÇO DE ENTREGA:
            CEP: {cep}
            Bairro: {neighborhood}
            Endereço: {address}
            Referência: {reference}
            -------------------------------------
            Acesse seu painel para gerenciar o pedido.
            """
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER, # Remetente
                ['claitonhgft@gmail.com'], # Destinatário (SEU EMAIL)
                fail_silently=False,
            )
            
            return redirect('order_success')
        except Exception as e:
            # Em caso de erro, mostre uma mensagem
            return render(request, 'store/order_form.html', {'product': product, 'error': f'Ocorreu um erro ao processar seu pedido: {e}'})


    return render(request, 'store/order_form.html', {'product': product})

# Página de Sucesso
def order_success(request):
    return render(request, 'store/order_success.html')