from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

#cada vista es una funcion y recibe un httprequest y devuelve una httpresponse


class Persona(object):
	def __init__(self,nombre,apellido):
		self.nombre=nombre
		self.apellido=apellido
		
	

def saludo(request): #esta es una vista, devuelve una respuesta
	
	p1=Persona("juan","diaz") #contexto
	
	#temas_curso=[] #prueba if else plantilla
	temas_curso=["Plantillas","Modelos","Formularios","Listas","Despliegues"]
	
	doc_externo=open(  "C:/Users/sebac/Desktop/ingenieria2/bookflix/bookflix/plantillas/miplantilla.html"  )
	plt=Template(doc_externo.read())
	doc_externo.close()
	cxt=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "temas":temas_curso}) #contexto recibe diccionarios
	documento=plt.render(cxt)
	return HttpResponse(documento)

def damefecha(request):
    fecha_actual=datetime.now()

    return HttpResponse(fecha_actual)

def calculaedad(request,edad,ano):
    ano_act=int(str(datetime.now()).split('-')[0])
    periodo=ano-ano_act
    edadfutura=edad+periodo
    return HttpResponse( "En el ano %s tendras %s " %(ano, edadfutura) )
