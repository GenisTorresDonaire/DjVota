from django.db import models
from django.conf import settings

# Create your models here.
class Preguntas(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    fechaFinal_pregunta = models.DateField()
    fechaInicial_pregunta = models.DateField()
    creador_pregunta = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
    	return self.texto_pregunta
 
class Opciones(models.Model):
    opcion_pregunta = models.CharField(max_length=200)
    def __str__(self):
    	return self.opcion_pregunta

class Voto(models.Model):
    id_opciones = models.IntegerField(max_length=200)
    id_usuario = models.IntegerField(max_length=200)

class Invitaciones(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)