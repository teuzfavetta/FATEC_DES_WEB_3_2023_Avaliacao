from django import forms
from .models import TaskModel
from django.forms import ModelForm

class TaskForm(ModelForm):
    PROFESSORES_CHOICES = [
        ('professor1', 'Orlando'),
        ('professor2', 'Nilton'),
        ('professor3', 'Thiago'),
    ]
    
    nome_professor = forms.ChoiceField(choices=PROFESSORES_CHOICES)
    
    
    class Meta:
        model = TaskModel
        fields = ['nome_aluno','nome_professor']
        error_messages = {
        'nome_aluno': {
            'required': ("Informe o nome do aluno."),
        }
    }
