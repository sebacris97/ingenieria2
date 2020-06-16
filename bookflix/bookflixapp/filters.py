import django_filters
from .models import Libro, Genero
from django import forms
from django.db import models

class LibroFilter(django_filters.FilterSet):


    class Meta:
        model = Libro
        fields = {
            'titulo': ['contains'], 'autor': ['exact'], 'editorial': ['exact'], 'genero': ['exact'], 'agnoedicion': ['exact']
        }
        filter_overrides = {
            models.ManyToManyField: {
                'filter_class': django_filters.ModelMultipleChoiceFilter,
                'extra': lambda f: {
                    'widget': forms.CheckboxSelectMultiple,
                    'queryset': Genero.objects.all()
                }
            }
        }
