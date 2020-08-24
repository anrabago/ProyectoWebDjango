from django.http import HttpResponse
import datetime
from django.template import Template, Context 
#from django.template import loader  
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

#primeras vistas
def saludo (request): 
    #nombre = "Antonio"
    #apellido = "García"
    p1 = Persona("Antonio", "García")

    #Ejemplo de como se cargaría una plantilla sin loader
    # doc_externo = open("C:/Users/anrab/source/repos/ProyectoWebDjango/ProyectoWebDjango/plantillas/miplantilla.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close()
    #ctx = Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "temas": ["Plantillas", "Modelos", "Formularios"]})
    #return HttpResponse (documento)
    
    #Usamos los cargadores de plantillas, para indicar la plantilla que vamos a utilizar. En settings.py indicamos la ruta de la carpeta de plantillas
    #doc_externo = get_template('miplantilla.html')
    #documento = doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "temas": ["Plantillas", "Modelos", "Formularios"]})
    #return HttpResponse (documento)

    #Usamos shotcuts para renderizar la plantilla
    return render(request, 'miplantilla.html', {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "temas": ["Plantillas", "Modelos", "Formularios"]})

def despedida(request):
    return HttpResponse("Hasta pronto")

def damefecha (request):
    fecha_actual = datetime.datetime.now()
    documento = """ <html><body>Fecha Actual: %s </body></html>""" % fecha_actual
    return HttpResponse(documento)

def calculaedad(request, edad, agno):    
    periodo = agno-2020
    edad_futura = edad + periodo
    documento = """ <html><body>En el año %s tendrás %s años </body></html>""" %(agno, edad_futura)
    return HttpResponse(documento)
