import datetime
import requests
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .forms import CustomUserCreationForm
from .decorators import role_required
from .models import Categoria, Marca, Producto, UserProfile, Client
from .serializers import CategoriaSerializer, MarcaSerializer, ProductoSerializer

# Create your views here.
def index_dyn(request):

    perfil = request.session.get('perfil')
    context = {
        'perfil': perfil
    }
    return render(request, 'index.html', context)

# vistas para las paginas del menu

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
            user = formularioregistro.save()
            UserProfile.objects.create(user=user, role='cliente')
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
def admincuenta_dyn(request):
    return render(request, 'menu/admincuenta.html')

@role_required('cliente', 'staff', 'admin')
def actualizar_datos_dyn(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, 'Datos actualizados correctamente.')
        return redirect('admincuenta_dyn')
    return render(request, 'menu/admincuenta.html', {'user': user})

@role_required('cliente', 'staff', 'admin')
def cambiar_contrasena_dyn(request):

    if request.method == 'POST':
        old_password = request.POST.get('oldPassword')
        new_password = request.POST.get('password')

        user = request.user

        # Verifica la contraseña actual
        if not user.check_password(old_password):
            messages.error(request, 'La contraseña actual es incorrecta.')
            return render(request, 'menu/admincuenta.html')

        # Cambia la contraseña
        user.set_password(new_password)
        user.save()
        logout(request)  # Cierra la sesión para que el usuario vuelva a iniciar sesión
        messages.success(request, 'Datos actualizados correctamente. Por favor, inicia sesión de nuevo.')
        return redirect('iniciosesion_dyn')

    return render(request, 'menu/admincuenta.html')

@role_required('cliente', 'staff', 'admin')
def cerrarsesion_dyn(request):
    logout(request)
    return redirect('iniciosesion_dyn')

@role_required('cliente', 'staff', 'admin')
def carrito_dyn(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0
    for producto_id, cantidad in carrito.items():
        producto = Producto.objects.get(id=producto_id)
        subtotal = producto.precio * cantidad
        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })
        total += subtotal
    contexto = {'productos': productos, 'total': total}
    return render(request, 'menu/carrito.html', contexto)

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

# definicion de api views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    respuesta = {
        'success': True,
        'message': 'Lista de categorías',
        'total': len(serializer.data),
        'time': datetime.datetime.now(),
        'data': serializer.data
    }
    return Response(respuesta)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    respuesta = {
        'success': True,
        'message': 'Lista de productos',
        'total': len(serializer.data),
        'time': datetime.datetime.now(),
        'data': serializer.data
    }
    return Response(respuesta)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_productos_categoria(request, idcategoria=None):
    try:
        categoria = Categoria.objects.get(id=idcategoria)
        productos = Producto.objects.filter(categoria_id=categoria)
        serializer = ProductoSerializer(productos, many=True)
        respuesta = {
            'success': True,
            'message': 'Lista de productos por categoría',
            'total': len(serializer.data),
            'time': datetime.datetime.now(),
            'data': serializer.data
        }
        return Response(respuesta)
    except Categoria.DoesNotExist:
        respuesta = {
            'success': False,
            'message': 'Categoría no encontrada',
            'time': datetime.datetime.now(),
            'data': []
        }
        return Response(respuesta, status=404)
    '''
    if idcategoria:
        productos = Producto.objects.filter(categoria_id=idcategoria)
    else:
        productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)
    '''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_marcas(request):
    marcas = Marca.objects.all()
    serializer = MarcaSerializer(marcas, many=True)
    respuesta = {
        'success': True,
        'message': 'Lista de marcas',
        'total': len(serializer.data),
        'time': datetime.datetime.now(),
        'data': serializer.data
    }
    return Response(respuesta)

# APIs externas de noticias
@api_view(['GET'])
def api_noticias_gaming(request):
    response = requests.get(
        url='https://newsapi.org/v2/everything?q=gaming&apiKey=9f8adec83c2949a796a8cd54c2c4f203'
    )
    noticias_gaming = []
    if response.status_code == 200:
        noticias_gaming = response.json()
    return Response(noticias_gaming)

@api_view(['GET'])
def api_noticias_games(request):
    response = requests.get(
        url='https://www.mmobomb.com/api1/latestnews'
    )
    noticias_juegos = []
    if response.status_code == 200:
        noticias_juegos = response.json()
    return Response(noticias_juegos)



@api_view(['POST'])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({
            'success': False,
            'message': 'Por favor, ingrese ambos campos: username y password.',
            'time': datetime.datetime.now(),
            'data': [],
            }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        respuesta = {
            'success': True,
            'message': 'Inicio de sesión exitoso.',
            'time': datetime.datetime.now(),
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }
        return Response(respuesta)
    else:
        return Response({
            'success': False,
            'message': 'Credenciales inválidas. Inténtelo de nuevo.',
            'time': datetime.datetime.now(),
            'data': []
        }, status=status.HTTP_401_UNAUTHORIZED)   


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_perfil_user(request):
    user = request.user
    perfil = UserProfile.objects.get(user=user)
    respuesta = {
        'success': True,
        'message': 'Perfil del usuario autenticado.',
        'time': datetime.datetime.now(),
        'data': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': perfil.role
        }
    }
    return Response(respuesta)

from django.shortcuts import get_object_or_404, redirect
from .models import Producto

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})

    # Si el producto ya está en el carrito, suma 1, si no, lo agrega
    if str(producto_id) in carrito:
        carrito[str(producto_id)] += 1
    else:
        carrito[str(producto_id)] = 1

    request.session['carrito'] = carrito
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER', 'ver_carrito'))

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
        request.session['carrito'] = carrito
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0
    for producto_id, cantidad in carrito.items():
        producto = Producto.objects.get(id=producto_id)
        subtotal = producto.precio * cantidad
        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })
        total += subtotal
    contexto = {'productos': productos, 'total': total}
    return render(request, 'menu/carrito.html', contexto)