from django.shortcuts import render
from .forms import FormularioAgregarLibro
from .models import Libro
from django.template import RequestContext


# Create your views here.
def agregar_libro(request):
    if request.method == 'POST':
        formularioLibro = FormularioAgregarLibro(request.POST)
        if formularioLibro.is_valid():
            titulo_libro = formularioLibro.cleaned_data['titulo_campo']
            nropaginas_libro = formularioLibro.cleaned_data['nropaginas_campo']
            nrocapitulos_libro = formularioLibro.cleaned_data['nrocapitulos_campo']
            isbn_libro = formularioLibro.cleaned_data['isbn_campo']
            autor_libro = formularioLibro.cleaned_data['autor_campo']
            editorial_libro = formularioLibro.cleaned_data['editorial_libro']
            genero_libro = formularioLibro.cleaned_data['genero_libro']
            agnoedicion_libro = formularioLibro.cleaned_data['agnoedicion_campo']
            nuevo_libro = Libro(titulo=titulo_libro, nropaginas=nropaginas_libro, nrocapitulos=nrocapitulos_libro, isbn=isbn_libro, autor=autor_libro, editorial=editorial_libro, agnoedicion=agnoedicion_libro)
            nuevo_libro.genero = genero_libro
            nuevo_libro.save()
            return render(request, "agregar_libro.html", {}, context_instance=RequestContext(request))
    else:
        formularioLibro = FormularioAgregarLibro()
    return render(request, "agregar_libro.html", {'formularioLibro': formularioLibro}, context_instance=RequestContext(request))
