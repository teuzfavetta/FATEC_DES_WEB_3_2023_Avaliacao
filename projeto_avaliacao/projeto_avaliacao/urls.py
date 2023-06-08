from django.urls import path
from core.views import cadastro, lista

urlpatterns = [
    path('', cadastro, name='cadastro'),
    path('lista', lista, name='lista'),
]
