from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, default='')

    def __str__(self):
        return '%s %s' % (self.apellido, self.nombre)


class Genero(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre


class Editorial(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    nropaginas = models.PositiveIntegerField()
    nrocapitulos = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero)
    agnoedicion = models.DateField()


class Novedad(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        return self.titulo
