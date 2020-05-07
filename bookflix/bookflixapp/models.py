from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=50)


class Genero(models.Model):
    nombre = models.CharField(max_length=25)


class Editorial(models.Model):
    nombre = models.CharField(max_length=200)


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    nropaginas = models.PositiveIntegerField()
    nrocapitulos = models.PositiveIntegerField()
    isbn = models.PositiveIntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genero = models.CharField(max_length=200)
    agnoedicion = models.DateField()
