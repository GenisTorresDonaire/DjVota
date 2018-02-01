from django.contrib import admin
from .models import Preguntas, Opciones, Voto, Invitaciones

class OpcionesInline(admin.StackedInline):
	model = Opciones
	extra = 3

# Register your models here.
class PreguntasAdmin(admin.ModelAdmin):
	list_display = ('texto_pregunta', 'creador_pregunta','fechaInicial_pregunta', 'fechaFinal_pregunta')
	readonly_fields = ('creador_pregunta',)
	def save_model(self, request, obj, form, change):
		obj.creador_pregunta = request.user
		super(PreguntasAdmin,self).save_model(request, obj, form, change)

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(creador_pregunta=request.user)
	inlines = [OpcionesInline]


class OpcionesAdmin(admin.ModelAdmin):
	list_display = ('opcion_pregunta', 'pregunta', 'creador')
	readonly_fields = ('pregunta',)
	def get_queryset(self, request):
		qs = Opciones.objects.all()
		if request.user.is_superuser:
			return qs
		return qs.filter(pregunta__creador_pregunta=request.user)

class InvitacionesAdmin(admin.ModelAdmin):
	list_display = ('usuario', 'pregunta')
	def get_queryset(self, request):
		qs = Invitaciones.objects.all()
		if request.user.is_superuser:
			return qs
		return qs.filter(usuario=request.user)

class VotoAdmin(admin.ModelAdmin):
	list_display = ('id_usuario', 'id_opciones')

admin.site.register(Preguntas, PreguntasAdmin)
admin.site.register(Opciones, OpcionesAdmin)
admin.site.register(Invitaciones, InvitacionesAdmin)
admin.site.register(Voto, VotoAdmin)