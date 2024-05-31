from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Citas
from .models import Empleado
from .models import Servicio
from .forms import CitasForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def libros(request):
    libros = Citas.objects.all()
    return render(request, 'libros/crud.html', {'libros': libros})

def crear(request):
    formulario = CitasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request,id):
    libro = Citas.objects.get(id=id)
    formulario = CitasForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = Citas.objects.get(id=id)
    libro.delete()
    return redirect('libros')

def empleado(request):
    libros = Empleado.objects.all()
    return render(request, 'libros/empleado.html', {'libros': libros})

def servicio(request):
    libros = Servicio.objects.all()
    return render(request, 'libros/servicio.html', {'libros': libros})

