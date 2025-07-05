# Este é o NOVO arquivo store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('produto/<int:product_id>/', views.product_detail, name='product_detail'),
    path('produto/<int:product_id>/pedido/', views.order_create, name='order_create'),
    path('pedido/sucesso/', views.order_success, name='order_success'),
]