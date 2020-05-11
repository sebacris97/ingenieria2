from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

#cada vista es una funcion y recibe un httprequest y devuelve una httpresponse


	

def saludo(request): #esta es una vista, devuelve una respuesta
	
	return HttpResponse("hola mundo")
