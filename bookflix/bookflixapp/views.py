from django.shortcuts import render
from .forms import FormularioAgregarLibro, FormularioAgregarNovedad
from .models import Libro, Novedad
from django.template import RequestContext


# Create your views here.

def index(request):
    return render(request,"index.html")

def agregar_libro(request):
    if request.method == 'POST':
        formularioLibro = FormularioAgregarLibro(request.POST)
        if formularioLibro.is_valid():
            titulo_libro = formularioLibro.cleaned_data['titulo_campo']
            nropaginas_libro = formularioLibro.cleaned_data['nropaginas_campo']
            nrocapitulos_libro = formularioLibro.cleaned_data['nrocapitulos_campo']
            isbn_libro = formularioLibro.cleaned_data['isbn_campo']
            autor_libro = formularioLibro.cleaned_data['autor_campo']
            editorial_libro = formularioLibro.cleaned_data['editorial_campo']
            genero_libro = formularioLibro.cleaned_data['genero_campo']
            agnoedicion_libro = formularioLibro.cleaned_data['agnoedicion_campo']
            nuevo_libro = Libro(titulo=titulo_libro, nropaginas=nropaginas_libro, nrocapitulos=nrocapitulos_libro, isbn=isbn_libro, autor=autor_libro, editorial=editorial_libro, agnoedicion=agnoedicion_libro)
            nuevo_libro.save()
            nuevo_libro.genero.add(*genero_libro)
            return render(request, "agregar_libro.html", {'formularioLibro': formularioLibro})
    else:
        formularioLibro = FormularioAgregarLibro()
    return render(request, "agregar_libro.html", {'formularioLibro': formularioLibro})


def agregar_novedad(request):
    if request.method == 'POST':
        formularioNovedad = FormularioAgregarNovedad(request.POST)
        if formularioNovedad.is_valid():
            titulo_novedad = formularioNovedad.cleaned_data['novedad_titulo_campo']
            texto_novedad = formularioNovedad.cleaned_data['novedad_texto_campo']
            nueva_novedad = Novedad(titulo=titulo_novedad, texto=texto_novedad)
            nueva_novedad.save()
            return render(request, "agregar_novedad.html", {'formularioNovedad': formularioNovedad})
    else:
        formularioNovedad = FormularioAgregarNovedad()
    return render(request, "agregar_novedad.html", {'formularioNovedad': formularioNovedad})


def ver_novedades(request):

    novedades=Novedad.objects.filter(titulo__icontains='') #__icontains es como like de sql
    return render(request,"ver_novedades.html",{"novedades":novedades})


def ver_libros(request):

    libros=Libro.objects.filter(titulo__icontains='') #__icontains es como like de sql
    return render(request,"ver_libros.html",{"libros":libros})
