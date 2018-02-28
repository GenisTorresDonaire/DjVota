from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Opciones, Preguntas, Voto


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Preguntas.objects.order_by('fechaFinal_pregunta')[:5]


class DetailView(generic.DetailView):
    model = Preguntas
    template_name = 'app/detail.html'


class ResultsView(generic.DetailView):
    model = Preguntas
    template_name = 'app/results.html'
    

def vote(request, question_id):
    preguntas = get_object_or_404(Preguntas, pk=question_id)
    try:
        seleccionOpcion = preguntas.opciones_set.get(pk=request.POST['opcion'])
    except (KeyError, Opciones.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'app/detail.html', {
            'preguntas': preguntas,
            'error_message': "You didn't select a choice.",
        })
    else:
        #seleccionOpcion.votes += 1
        v = Voto()
        #v.id_usuario = request.user
        v.id_opciones = seleccionOpcion
        v.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app:results', args=(preguntas.id,)))

