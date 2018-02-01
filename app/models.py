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
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    def creador(self):
        return self.pregunta.creador_pregunta
    def __str__(self):
        return self.opcion_pregunta
    def __unicode__(self):
        return self.title

class Invitaciones(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)    

class Voto(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_opciones = models.ForeignKey(Opciones, on_delete=models.CASCADE)



































#def votos(self):
#    votos = vot.objects.filter(opcion=self.id).count()
#    return votos




#enviada = models.BooleanField(default=False)
#aceptada = models.BooleanField(default=False)
#def __unicode__(self):
#    return self.pregunta + " | " + self.usuario
#def __str__(self):
#    return self.__unicode__()
