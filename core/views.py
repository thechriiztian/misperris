from django.shortcuts import render, redirect
from .models import Raza, Estado, Mascota
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def formularioMascota(request):
    #IMPORTANTEEEE¡¡¡¡¡¡¡¡
    razas = Raza.objects.all()
    
    variables = {
        'razas': razas  
    }

    if request.POST:
        mascota = Mascota()
        mascota.nombre = request.POST.get('txtNombre')
        mascota.genero = request.POST.get('txtGenero')
        mascota.fechaIngreso = request.POST.get('dFechaIngreso')
        mascota.fechaNac = request.POST.get('dFechaNac')
        mascota.descripcion = request.POST.get('txtDescripcion')
        
        raza = Raza()
        raza.id = int(request.POST.get('cboRaza'))
        mascota.raza = raza

        try:
            mascota.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido Guardar'

    return render(request, 'core/formularioMascota.html',variables)

#CRUD de mascota

def listar_mascotas(request):

    mascota = Mascota.objects.all()

    return render(request, 'core/listar_mascotas.html', {
        'mascota':mascota
    })

def eliminar_mascota(request,id):
    #buscar mascota
    auto = Mascota.objects.get(id = id)

    try:
        auto.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.success(request, mensaje)

    return redirect('listado_mascotas')
