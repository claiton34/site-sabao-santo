# Este é o arquivo sabao_livre/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# A linha "from . import views" foi REMOVIDA daqui.
from django.conf.urls.static import static

urlpatterns = [
    path('painel-vendedor/', admin.site.urls),
    path('', include('store.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)