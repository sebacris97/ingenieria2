from django.db import models

# Create your models here.
class libro(models.Model):
	titulo=models.CharField(max_length=200)
	nropaginas=models.PositiveIntegerField()
	nrocapitulos=models.PositiveIntegerField()
	isbn=models.PositiveIntegerField()
	autor=models.CharField(max_length=200)
	editorial=models.CharField(max_length=200)
	genero=models.CharField(max_length=200)
	agnoedicion=models.DateField()