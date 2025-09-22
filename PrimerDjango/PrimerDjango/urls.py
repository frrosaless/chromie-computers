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
from django.urls import path

from core.views import index_dyn, registro_dyn, iniciosesion_dyn, carrito_dyn, admincuenta_dyn, olvidecontrasena_dyn

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_dyn, name="index_dyn"),
    path("registro/", registro_dyn, name="registro_dyn"),
    path("iniciosesion/", iniciosesion_dyn, name="iniciosesion_dyn"),
    path("carrito/", carrito_dyn, name="carrito_dyn"),
    path("admincuenta/", admincuenta_dyn, name="admincuenta_dyn"),
    path("olvidecontrasena/", olvidecontrasena_dyn, name="olvidecontrasena_dyn"),
]
