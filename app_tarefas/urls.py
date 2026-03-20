from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_tarefa, name="home"),
    path("concluir/<int:tarefa_id>/", views.concluir_tarefa, name="concluir_tarefa"),
    path("deletar/<int:tarefa_id>/", views.deletar_tarefa, name="deletar_tarefa"),
]