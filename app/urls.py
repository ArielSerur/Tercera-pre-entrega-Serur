from django.urls import path 
from app import views 

urlpatterns = [ 
    path("", views.inicio),
    path("alta-cliente/", views.crear_cliente,name="AltaCliente"),
    path("alta-producto/", views.crear_producto,name="AltaProducto"),
    path("alta-publicacion/", views.crear_publicacion,name="AltaPublicacion"),
    path("buscar-cliente/", views.buscar_cliente,name="BuscadorCliente") 
]
