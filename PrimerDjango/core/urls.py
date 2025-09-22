from django.urls import path
from . import views

urlpatterns = [
    path('producto/', views.lista_productos, name='lista_productos'),
    path('producto/lista', views.lista_dual, name='lista_dual'),
    path('producto/crear', views.crear_producto, name='crear_producto'),
    path('producto/crearmarca', views.crear_marca, name='crear_marca'),
    path('producto/crearcategoria', views.crear_categoria, name='crear_categoria'),
    path('producto/<int:id>/editar', views.editar_producto, name='editar_producto'),
    path('producto/<int:id>/eliminar', views.eliminar_producto, name='eliminar_producto'),
    path('producto/<int:id>/editarmarca', views.editar_marca, name='editar_marca'),
    path('producto/<int:id>/eliminarmarca', views.eliminar_marca, name='eliminar_marca'),
    path('producto/<int:id>/editarcategoria', views.editar_categoria, name='editar_categoria'),
    path('producto/<int:id>/eliminarcategoria', views.eliminar_categoria, name='eliminar_categoria'),
]