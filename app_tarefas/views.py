from django.shortcuts import render, redirect
from .models import Tarefa

# Create your views here.
def lista_tarefa(request):
    if request.method == 'POST':
        novo_titulo = request.POST.get('novo_titulo')
        if novo_titulo:
            Tarefa.objects.create(titulo=novo_titulo)
        return redirect('home')

    minhas_tarefas = Tarefa.objects.all()

    contexto = {
        'tarefas': minhas_tarefas
    }

    return render(request, 'lista.html', contexto)

def concluir_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('home')

def deletar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    return redirect('home')
