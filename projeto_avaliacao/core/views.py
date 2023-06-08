from datetime import date
from django.shortcuts import redirect, render

from core.forms import TaskForm
from core.models import TaskModel


def cadastro(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista.html')
    else:
        form = TaskForm()
    return render(request, 'cadastro.html', {'form': form})

def lista(request):
    alunos = TaskModel.objects.filter(modificado_em=date.today())
    return render(request, 'lista.html', {'alunos': alunos})