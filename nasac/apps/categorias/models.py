from django.db import models

# Create your models here.
from apps.core.models import TimeModel

class Categoria(TimeModel):
	nombre= models.CharField(max_length = 30)
	cantidad_preguntas= models.IntegerField(default = 0)

	def __str__(self):
		return self.nombre