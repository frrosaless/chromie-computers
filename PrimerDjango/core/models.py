from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
# categoria, marca, producto, proveedor, cliente, venta, detalle venta
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    birthdate = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.firstname

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente.firstname}"
    
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.venta}"
    
# Relaciones:
# Producto -> Categoria (Many to One)
# Producto -> Marca (Many to One)
# Producto -> Proveedor (Many to One)
# Venta -> Cliente (Many to One)
# DetalleVenta -> Venta (Many to One)
# DetalleVenta -> Producto (Many to One)

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES, default='cliente')

    def __str__(self):
        return f"{self.user.username} - {self.role}"