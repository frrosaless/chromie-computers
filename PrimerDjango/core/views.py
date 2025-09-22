from django.shortcuts import render

# Create your views here.
def index_dyn(request):
    return render(request, 'index.html')

def registro_dyn(request):
    return render(request, 'menu/registro.html')

def iniciosesion_dyn(request):
    return render(request, 'menu/iniciosesion.html')

def carrito_dyn(request):
    return render(request, 'menu/carrito.html')

def admincuenta_dyn(request):
    return render(request, 'menu/admincuenta.html')

def olvidecontrasena_dyn(request):
    return render(request, 'menu/olvidecontrasena.html')