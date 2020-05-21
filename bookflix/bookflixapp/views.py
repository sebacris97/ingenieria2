from django.shortcuts import render, redirect
from bookflixapp.models import Libro, Novedad, Capitulo, Perfil, Usuario, UsuarioCust
from datetime import timedelta
from django.utils import timezone
from django.http import request as rq

from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from .forms import RegistrationForm, CreateProfileForm

# from .forms import FormularioAgregarLibro

# Create your views here.


"""
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
"""


def ver_libros(request):
    libros = Libro.objects.all()
    return render(request, "ver_libros.html", {"libros": libros})


def ver_capitulos(request, pk):
    capitulos = Capitulo.objects.filter(libro__id=pk)
    if len(capitulos) > 0:  # parche temporal para los libros que no tienen capitulos
        titulo = capitulos[0].libro
        # el parametro lo recibe de urls. lo que hago es filtrar los capitulos
        # que pertenecen al libro que recibo como parametro
        # (si hiciese objects.all() me estoy quedando con todos los capitulos de todos los libros)
        return render(request, "ver_capitulos.html", {"capitulos": capitulos, "titulo": titulo})
    else:
        return render(request, "index.html")  # si no se le subio capitulo te manda a index


def index(request):
    d = timezone.now() - timedelta(days=7)
    f = timezone.now()
    delt = timedelta(days=7)
    aux = d.date()
    novedades = Novedad.objects.filter(creacion__gte=d)
    return render(request, "index.html", {"novedades": novedades})


def register(request):
    # Creamos el formulario de autenticación vacío
    form = RegistrationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = RegistrationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            username = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            tarjeta = form.cleaned_data["tarjeta"]
            fecha = form.cleaned_data["fecha_de_nacimiento"]
            u = User(username=username, first_name=first_name, last_name=last_name, password=password1, email=username)
            u.save()
            user = Usuario(user=u, fecha_de_nacimiento=fecha, tarjeta=tarjeta)
            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                user.save()
                do_login(request, u)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si queremos borramos los campos de ayuda
    #form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)

                if user.is_superuser:
                    return redirect("/admin")  # or your url name

                # Y le redireccionamos a la portada
                return redirect('/')
                #return render(request, "index.html")

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/login/')


def createprofile(request):
    if request.method == "POST":
        form = CreateProfileForm(data=request.POST)
        if form.is_valid():
            profilename = form.cleaned_data["profilename"]
            user = request.user
            usuario = Usuario.objects.get(user=user)
            profile = Perfil(usuario=usuario, username=profilename)
            profile.save()
            if profile is not None:
                return redirect("/")
    else:
        form = CreateProfileForm()
        return render(request, "crear_perfil.html", {'form': form})


def verperfil(request):
    user = request.user
    usuario = Usuario.objects.get(user=user)
    perfil = Perfil.objects.filter(usuario=usuario)
    return render(request, 'perfil.html', {"perfil": perfil[1]})


