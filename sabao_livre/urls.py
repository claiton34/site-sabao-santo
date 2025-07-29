from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # <-- ADICIONE ESTA LINHA DE IMPORTAÇÃO

urlpatterns = [
    path('painel-vendedor/', admin.site.urls),
    path('', include('store.urls')),

    # ROTAS PARA RECUPERAÇÃO DE SENHA
    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="store/password_reset_form.html"), 
        name="reset_password"),
    
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="store/password_reset_done.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="store/password_reset_confirm.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="store/password_reset_complete.html"), 
        name="password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
