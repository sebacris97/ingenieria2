from django.db import models
from django.core.validators import RegexValidator

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, default='')

    def __str__(self):
        return '%s %s' % (self.apellido, self.nombre)

    class Meta:
        verbose_name_plural = "Autores"


class Genero(models.Model):
    nombre = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Generos"


class Editorial(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Editoriales"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    nropaginas = models.PositiveIntegerField(verbose_name="Numero de paginas")
    nrocapitulos = models.PositiveIntegerField(verbose_name="Numero de capitulos")
    isbn = models.CharField(max_length=13,unique=True,validators=[RegexValidator('^(\d{10}|\d{13})$', 'El numero debe tener 10 o 13 digitos numericos')],verbose_name="ISBN")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero)
    agnoedicion = models.DateField(verbose_name="Año de edicion")   
    pdf = models.FileField(upload_to='libros')


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Libros"


        

class Novedad(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True,verbose_name="Creacion")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Novedades"


