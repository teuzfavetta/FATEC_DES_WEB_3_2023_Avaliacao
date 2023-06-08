from django.test import TestCase
from django.urls import reverse
from core.models import TaskModel

class AlunoModelTest(TestCase):
    def test_str_representation(self):
        aluno = TaskModel(nome='João', professor='Orlando')
        self.assertEqual(str(aluno), 'João')

class CadastrarPresencaViewTest(TestCase):
    def test_cadastro_get(self):
        url = reverse('cadastro')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_cadastro_post(self):
        url = reverse('cadastro')
        data = {
            'nome': 'Maria',
            'professor': 'Nilton',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista'))
        self.assertEqual(TaskModel.objects.count(), 1)
        self.assertEqual(TaskModel.objects.first().nome, 'Maria')
