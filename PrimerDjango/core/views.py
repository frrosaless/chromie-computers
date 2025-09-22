from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import role_required

from .forms import CustomUserCreationForm

from .models import Categoria, Marca, Producto, UserProfile

# Create your views here.
def index_dyn(request):

    perfil = request.session.get('perfil')
    context = {
        'perfil': perfil
    }
    return render(request, 'index.html', context)

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
                profile = UserProfile.objects.get(user=username)
                request.session['perfil'] = profile.role
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

    

@role_required('cliente', 'staff', 'admin')
def cerrarsesion_dyn(request):
    logout(request)
    return redirect('iniciosesion_dyn')

@role_required('cliente', 'staff', 'admin')
def carrito_dyn(request):
    return render(request, 'menu/carrito.html')

@role_required('cliente', 'staff', 'admin')
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

@role_required('staff', 'admin')
def lista_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'productos/productos.html', context)

@role_required('staff', 'admin')
def lista_dual(request):
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    context = {
        'categorias': categorias,
        'marcas': marcas
    }    
    return render(request, 'productos/listado.html', context)

@role_required('staff', 'admin')
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
        messages.success(request, 'Producto creado correctamente.')
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    context = {
        'categorias': categorias,
        'marcas': marcas
    }
    return render(request, 'productos/crearproductos.html', context)

@role_required('staff', 'admin')
def crear_marca(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Marca.objects.create(nombre=nombre)
        messages.success(request, 'Marca creada correctamente.')
    return render(request, 'productos/crearmarca.html')

@role_required('staff', 'admin')
def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        imagen = request.FILES.get('imagen')
        Categoria.objects.create(nombre=nombre, imagen=imagen)
        messages.success(request, 'Categoría creada correctamente.')
    return render(request, 'productos/crearcat.html')

@role_required('staff', 'admin')
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
        messages.success(request, 'Producto actualizado correctamente.')

    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    context = {
        'producto': producto,
        'categorias': categorias,
        'marcas': marcas
    }
    return render(request, 'productos/editarproductos.html', context)

@role_required('staff', 'admin')
def editar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)

    if request.method == 'POST':
        marca.nombre = request.POST.get('nombre')
        marca.save()
        messages.success(request, 'Marca actualizada correctamente.')
    context = {
        'marca': marca
    }
    return render(request, 'productos/editarmarca.html', context)

@role_required('staff', 'admin')
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        if 'imagen' in request.FILES:
            categoria.imagen = request.FILES['imagen']
        categoria.save()
        messages.success(request, 'Categoría actualizada correctamente.')
    context = {
        'categoria': categoria
    }
    return render(request, 'productos/editarcat.html', context)

@role_required('staff', 'admin')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, 'Producto eliminado correctamente.')
    return redirect('lista_productos')

@role_required('staff', 'admin')
def eliminar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    messages.success(request, 'Marca eliminada correctamente.')

    return redirect('lista_dual')

@role_required('staff', 'admin')
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, 'Categoría eliminada correctamente.')

    return redirect('lista_dual')