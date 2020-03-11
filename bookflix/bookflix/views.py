from django.http import HttpResponse
import datetime

#cada vista es una funcion y recibe un httprequest y devuelve una httpresponse
def saludo(request): #esta es una vista, devuelve una respuesta
    return HttpResponse("hola alumnos como les va")

def damefecha(request):
    fecha_actual=datetime.datetime.now()

    return HttpResponse(fecha_actual)

def calculaedad(request,ano):
    edad_act=22
    periodo=ano-2019
    edadfutura=edad_act+periodo
    return HttpResponse( "En el ano %s tendras %s " %(ano, edadfutura) )
