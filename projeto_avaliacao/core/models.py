from django.db import models

class TaskModel(models.Model):
    nome_aluno = models.CharField('Aluno',max_length=50)
    nome_professor = models.CharField('Professor',max_length=50)
    modificado_em = models.DateTimeField(
        verbose_name= 'Modificado_em', 
        auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Alunos'
        verbose_name = 'Aluno'
        ordering = ('nome_aluno','-nome_professor')



    def __str__(self):
        return self.nome_aluno
