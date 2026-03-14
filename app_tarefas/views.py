from django.shortcuts import render
from .models import Tarefa

# Create your views here.
def lista_tarefa(request):
    minhas_tarefas = Tarefa.objects.all()

    contexto = {
        'tarefas': minhas_tarefas
    }

    return render(request, 'lista.html', contexto)
