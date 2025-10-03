"""
URL configuration for PrimerDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import index_dyn, registro_dyn, iniciosesion_dyn, cerrarsesion_dyn, carrito_dyn, admincuenta_dyn, olvidecontrasena_dyn, almacenamiento_dyn
from core.views import fuentes_dyn, gabinetes_dyn, memorias_dyn, placasmadres_dyn, procesadores_dyn, tarjetasdevideo_dyn, almace_wd_dyn
from core.views import fuente_giga_dyn, gab_antec_dyn, placa_giga_dyn, proce_intel_dyn, ram_king_dyn, video_giga_dyn, api_categorias, api_productos_categoria
from core.views import api_marcas, api_noticias_gaming, api_noticias_games, api_productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_dyn, name="index_dyn"),
    path("registro/", registro_dyn, name="registro_dyn"),
    path("iniciosesion/", iniciosesion_dyn, name="iniciosesion_dyn"),
    path("carrito/", carrito_dyn, name="carrito_dyn"),
    path("admincuenta/", admincuenta_dyn, name="admincuenta_dyn"),
    path("olvidecontrasena/", olvidecontrasena_dyn, name="olvidecontrasena_dyn"),
    path("almacenamiento/", almacenamiento_dyn, name="almacenamiento_dyn"),
    path("fuentes/", fuentes_dyn, name="fuentes_dyn"),
    path("gabinetes/", gabinetes_dyn, name="gabinetes_dyn"),
    path("memorias/", memorias_dyn, name="memorias_dyn"),
    path("placasmadres/", placasmadres_dyn, name="placasmadres_dyn"),
    path("procesadores/", procesadores_dyn, name="procesadores_dyn"),
    path("tarjetasdevideo/", tarjetasdevideo_dyn, name="tarjetasdevideo_dyn"),
    path("almace-wd/", almace_wd_dyn, name="almace_wd_dyn"),
    path("fuente-giga/", fuente_giga_dyn, name="fuente_giga_dyn"),
    path("gab-antec/", gab_antec_dyn, name="gab_antec_dyn"),
    path("placa-giga/", placa_giga_dyn, name="placa_giga_dyn"),
    path("proce-intel/", proce_intel_dyn, name="proce_intel_dyn"),
    path("ram-king/", ram_king_dyn, name="ram_king_dyn"),
    path("video-giga/", video_giga_dyn, name="video_giga_dyn"),
    path("cerrar_sesion/", cerrarsesion_dyn, name="cerrarsesion_dyn"),
    path('', include('core.urls')),
    path('api/categorias/', api_categorias, name='api_categorias'),
    path('api/productos/categoria/<int:idcategoria>/', api_productos_categoria, name='api_productos_por_categoria'),
    path('api/marcas/', api_marcas, name='api_marcas'),
    path('api/noticias/gaming/', api_noticias_gaming, name='api_noticias_gaming'),
    path('api/noticias/games/', api_noticias_games, name='api_noticias_games'),
    path('api/productos/', api_productos, name='api_productos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
