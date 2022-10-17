from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render,redirect
import random

from home.models import Persona

def hola(request):
    return HttpResponse('<h2>Buenas clase</h2>')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La hora y fecha actual es {fecha_actual}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años es: {fecha}')

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\Pablo\Desktop\Proyecto_ PabloNicolasConsiglio\proyecto_primero-main\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

def crear_persona(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
        persona.save()
        return redirect('personas_casamiento')
    return render(request, 'crear_persona.html', {})
    
def personas_casamiento(request):
    
    personas = Persona.objects.all()
    
    # template = loader.get_template('ver_personas.html')
    # template_renderizado = template.render({'personas': personas})
    
    # return HttpResponse(template_renderizado)
    return render(request, 'ver_personas.html', {'personas': personas})

def index(request):
    return render(request, 'index.html')