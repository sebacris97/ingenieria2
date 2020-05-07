from django import forms
from django.core.exceptions import ValidationError


class FormularioAgregarLibro(forms.Form):
    titulo_campo = forms.CharField(required=True, label='Titulo: ')
    nropaginas_campo = forms.IntegerField(required=True, label='Numero De Paginas: ')
    def clean_nropaginas_campo(self):
        data = self.cleaned_data['nropaginas_campo']
        if data < 1:
            raise ValidationError('El nro de paginas debe ser como minimo 1')
    return data
    nrocapitulos_campo = forms.IntegerField(required=True, label='Numero De Capitulos: ')
    isbn_campo = forms.CharField(required=True, label='ISBN: ', help_text='Introduzca ISBN de 13 numeros sin el guion')
    def clean_isbn_campo(self):
        data = self.cleaned_data['isbn_campo']
        if len(data) != 13:
            raise ValidationError('El ISBN ingresado no tiene 13 numeros')
    return data
    autor_campo = forms.ChoiceField(required=True, label='Autor: ')
    editorial_campo = forms.ChoiceField(required=True, label='Editorial: ')
    genero_campo = forms.MultipleChoiceField(required=True, label='Genero: ')
    agnoedicion_campo = forms.DateField(required=True, label='Fecha de Edicion: ')
