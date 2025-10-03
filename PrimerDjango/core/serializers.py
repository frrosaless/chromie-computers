from rest_framework import serializers
from .models import Categoria, Marca, Producto, Cliente

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'imagen']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre']

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    marca = MarcaSerializer(read_only=True)
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'marca', 'imagen']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'username', 'firstname', 'lastname', 'address', 'birthdate', 'email']
