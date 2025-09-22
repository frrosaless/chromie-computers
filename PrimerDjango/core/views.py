from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

from .models import Categoria, Marca, Producto

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

def lista_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'productos/productos.html', context)

def lista_dual(request):
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    context = {
        'categorias': categorias,
        'marcas': marcas
    }    
    return render(request, 'productos/listado.html', context)

def crear_producto(request):
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        marca_id = request.POST.get('marca')
        categoria = get_object_or_404(Categoria, id=categoria_id)
        marca = get_object_or_404(Marca, id=marca_id)

        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        imagen = request.FILES.get('imagen')

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            marca=marca,
            imagen=imagen
        )
        return redirect('lista_productos')
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    context = {
        'categorias': categorias,
        'marcas': marcas
    }
    return render(request, 'productos/crearproductos.html', context)

def crear_marca(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Marca.objects.create(nombre=nombre)
        return redirect('lista_dual')
    return render(request, 'productos/crearmarca.html')

def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        imagen = request.FILES.get('imagen')
        Categoria.objects.create(nombre=nombre, imagen=imagen)
        return redirect('lista_dual')
    return render(request, 'productos/crearcat.html')

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        marca_id = request.POST.get('marca')
        categoria = get_object_or_404(Categoria, id=categoria_id)
        marca = get_object_or_404(Marca, id=marca_id)

        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.categoria = categoria
        producto.marca = marca

        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']

        producto.save()

    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    context = {
        'producto': producto,
        'categorias': categorias,
        'marcas': marcas
    }
    return render(request, 'productos/editarproductos.html', context)

def editar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)

    if request.method == 'POST':
        marca.nombre = request.POST.get('nombre')
        marca.save()

    context = {
        'marca': marca
    }
    return render(request, 'productos/editarmarca.html', context)

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        if 'imagen' in request.FILES:
            categoria.imagen = request.FILES['imagen']
        categoria.save()

    context = {
        'categoria': categoria
    }
    return render(request, 'productos/editarcat.html', context)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()

    return redirect('lista_productos')

def eliminar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()

    return redirect('lista_dual')

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()

    return redirect('lista_dual')