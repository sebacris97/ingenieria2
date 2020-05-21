from django import forms
from django.core.exceptions import ValidationError
from .models import Autor, Editorial, Genero, Usuario, UsuarioCust
from datetime import datetime as d
from django.contrib.auth.forms import UserCreationForm
from django.http import request


class FormularioAgregarLibro(forms.Form):
    titulo_campo = forms.CharField(required=True, label='Titulo')
    nropaginas_campo = forms.IntegerField(required=True, label='Numero De Paginas')

    def clean_nropaginas_campo(self):
        data = self.cleaned_data['nropaginas_campo']
        if data < 1 or data > 2147483647:
            raise ValidationError('El nro de paginas debe ser como minimo 1 y como maximo 2147483647')
        return data

    nrocapitulos_campo = forms.IntegerField(required=True, label='Numero De Capitulos')

    def clean_nrocapitulos_campo(self):
        data = self.cleaned_data['nrocapitulos_campo']
        if data < 0 or data > 2147483647:
            raise ValidationError('El nro de capitulos debe ser como minimo 0 y como maximo 2147483647')
        return data

    isbn_campo = forms.CharField(required=True, label='ISBN', help_text='Introduzca ISBN de 13 numeros sin el guion')

    def clean_isbn_campo(self):
        data = self.cleaned_data['isbn_campo']
        if (10 != len(data) != 13) or not data.isdigit():
            raise ValidationError('El ISBN ingresado no tiene 13 numeros')
        return data

    autor_campo = forms.ModelChoiceField(queryset=Autor.objects.all(), initial=0, required=True, label='Autor')
    editorial_campo = forms.ModelChoiceField(queryset=Editorial.objects.all(), initial=0, required=True,
                                             label='Editorial')
    genero_campo = forms.ModelMultipleChoiceField(queryset=Genero.objects.all(), widget=forms.CheckboxSelectMultiple,
                                                  initial=0, required=True, label='Genero')
    today = str(str(d.now().year) + '-' + str(d.now().month) + '-' + str(d.now().day))
    agnoedicion_campo = forms.DateField(required=True,
                                        widget=forms.SelectDateWidget(years=range(1700, (int(d.now().year)) + 1)),
                                        initial=today, label='Fecha de Edicion')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    tarjeta = forms.CharField(required=True, max_length=16, min_length=16)
    fecha_de_nacimiento = forms.DateField(required=True)

    class Meta:
        model = UsuarioCust
        fields = ("first_name",
                  "last_name",
                  "fecha_de_nacimiento",
                  "email",
                  "password1",
                  "password2",
                  "tarjeta",
                  )


class CreateProfileForm(forms.Form):
    profilename = forms.CharField(required=True, label="Nombre de Perfil")
