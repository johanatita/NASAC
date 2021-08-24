from django.db import models

# Create your models here.
from apps.core.models import TimeModel
from apps.categorias.models import Categoria

class Pregunta(TimeModel):
	nombre= models.CharField(max_length = 100)
	puntaje= models.IntegerField(default = 0)
	categorias = models.ForeignKey(Categoria, related_name = 'mi_categoria', on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.nombre
	def getPuntaje(self,puntaje):
		return self.puntaje