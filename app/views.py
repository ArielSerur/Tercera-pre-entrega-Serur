from django.shortcuts import render
from app.models import Cliente
from .forms import PublicacionForm, ClienteForm, ProductoForm , BuscadorCliente

# Create your views here.
def inicio(request):
    return render (request, "app/index.html")

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/exito.html')
    else:
        form = ClienteForm()
    return render(request, 'app/clientes.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/exito.html')
    else:
        form = ProductoForm()
    return render(request, 'app/productos.html', {'form': form})

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/exito.html')
    else:
        form = PublicacionForm()
    return render(request, 'app/publicaciones.html', {'form': form})

def buscar_cliente(request):
    if request.method == "POST":
        mi_formulario = BuscadorCliente(request.POST)
        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            
            clientes = Cliente.objects.filter(nombre__icontains=informacion["cliente"])

            return render(request, 'app/encontrar_cliente.html',{
                "clientes": clientes
            })
    else:
        mi_formulario = BuscadorCliente() 
    return render(request, 'app/buscador.html', {'form': mi_formulario}) 