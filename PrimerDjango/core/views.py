from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

# Create your views here.
def index_dyn(request):
    return render(request, 'index.html')

# vistas para las paginas del menu
def registro_dyn(request):
    return render(request, 'menu/registro.html')

def iniciosesion_dyn(request):
    if request.method == 'POST':
        forminiciosesion = AuthenticationForm(data=request.POST)
        if forminiciosesion.is_valid():
            username = forminiciosesion.cleaned_data.get('username')
            password = forminiciosesion.cleaned_data.get('password')
            username = authenticate(username=username, password=password)
            if username is None:
                context = {
                    'forminiciosesion': forminiciosesion,
                    'error': "Usuario o contraseña incorrectos"
                }
                return render(request, 'menu/iniciosesion.html', context)
            else:
                login(request, username)
                return redirect('index_dyn')
        else:
            context = {
                'forminiciosesion': forminiciosesion,
                'error': "Usuario o contraseña incorrectos"
            }
            return render(request, 'menu/iniciosesion.html', context)
    else:
        forminiciosesion = AuthenticationForm()
        context = {
            'forminiciosesion': forminiciosesion
        }
    return render(request, 'menu/iniciosesion.html', context)

def registro_dyn(request):
    if request.method == 'POST':
        formularioregistro = CustomUserCreationForm(request.POST)
        if formularioregistro.is_valid():
            formularioregistro.save()
            return redirect('iniciosesion_dyn')
        else:
            contexto = {
                'formularioregistro': formularioregistro
            }
            return render(request, 'menu/registro.html', contexto)
    else:
        formularioregistro = CustomUserCreationForm()
        contexto = {
            'formularioregistro': formularioregistro
        }
        return render(request, 'menu/registro.html', contexto)

    

@login_required
def cerrarsesion_dyn(request):
    logout(request)
    return redirect('index_dyn')

def carrito_dyn(request):
    return render(request, 'menu/carrito.html')

def admincuenta_dyn(request):
    return render(request, 'menu/admincuenta.html')

def olvidecontrasena_dyn(request):
    return render(request, 'menu/olvidecontrasena.html')

# vistas para las paginas de las categorias
def almacenamiento_dyn(request):
    return render(request, 'categorias/almacenamiento.html')

def fuentes_dyn(request):
    return render(request, 'categorias/fuentes.html')

def gabinetes_dyn(request):
    return render(request, 'categorias/gabinetes.html')

def memorias_dyn(request):
    return render(request, 'categorias/memoriasram.html')

def placasmadres_dyn(request):
    return render(request, 'categorias/placasmadre.html')

def procesadores_dyn(request):
    return render(request, 'categorias/procesadores.html')

def tarjetasdevideo_dyn(request):
    return render(request, 'categorias/tarjetasdevideo.html')

# vistas para las paginas de las especificaciones
def almace_wd_dyn(request):
    return render(request, 'categorias/especificaciones/almace-wd.html')

def fuente_giga_dyn(request):
    return render(request, 'categorias/especificaciones/fuente-giga.html')

def gab_antec_dyn(request):
    return render(request, 'categorias/especificaciones/gab-antec.html')

def placa_giga_dyn(request):
    return render(request, 'categorias/especificaciones/placa-giga.html')

def proce_intel_dyn(request):
    return render(request, 'categorias/especificaciones/proce-intel.html')

def ram_king_dyn(request):
    return render(request, 'categorias/especificaciones/ram-king.html')

def video_giga_dyn(request):
    return render(request, 'categorias/especificaciones/video-giga.html')

#autenticaciones
