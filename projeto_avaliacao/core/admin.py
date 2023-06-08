from django.contrib import admin
from datetime import date

from core.models import TaskModel

class AlunoModelAdmin(admin.ModelAdmin):
    list_display = ('nome_aluno','nome_professor', 'modificado_em')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome_aluno','nome_professor')
    list_filter = ('modificado_em',)

admin.site.register(TaskModel,AlunoModelAdmin)
