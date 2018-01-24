from django.contrib import admin

from .models import Preguntas, Opciones, Voto, Invitaciones

# Register your models here.
admin.site.register(Preguntas)
admin.site.register(Opciones)
admin.site.register(Voto)
admin.site.register(Invitaciones)
