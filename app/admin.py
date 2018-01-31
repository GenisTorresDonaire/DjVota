from django.contrib import admin
from .models import Preguntas, Opciones, Voto, Invitaciones

class OpcionesInline(admin.StackedInline):
	model = Opciones
	extra = 3

# Register your models here.
class PreguntasAdmin(admin.ModelAdmin):
	list_display = ('texto_pregunta', 'creador_pregunta','fechaInicial_pregunta', 'fechaFinal_pregunta')
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(creador_pregunta=request.user)
	inlines = [OpcionesInline]


class OpcionesAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(creador_pregunta=request.user)

class InvitacionesAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(creador_pregunta=request.user)

admin.site.register(Preguntas, PreguntasAdmin)
admin.site.register(Opciones, OpcionesAdmin)
admin.site.register(Invitaciones, InvitacionesAdmin)
admin.site.register(Voto)