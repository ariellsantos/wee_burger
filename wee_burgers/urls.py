from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from basicos import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^usuarios/', include('usuarios.urls')),
    url(r'^ventas/',  include('venta.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)