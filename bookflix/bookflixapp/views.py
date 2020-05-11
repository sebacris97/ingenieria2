from django.shortcuts import render
from .forms import FormularioAgregarLibro
from .models import Libro


# Create your views here.

def index(request):
    return render(request, "index.html")


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
