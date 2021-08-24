from django.db import models

# Create your models here.
from apps.core.models import TimeModel
from apps.preguntas.models import Pregunta

class Respuesta(TimeModel):
	nombre= models.CharField(max_length = 100)
	puntaje= models.IntegerField(default = 0)
	preguntas = models.ForeignKey(Pregunta, on_delete = models.SET_NULL , null = True)
	def __str__(self):
		return self.nombre
	def getPuntaje(self,puntaje):
		return self.puntaje