from django.urls import path
from . import views
from .views import BilheteList

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("htmx/bilhete/informacao", views.bilhete_informacao, name="informacao"),
    path("htmx/bilhete/informacao/detalhes", views.bilhete_informacao_detalhes, name="detalhes"),
    path("htmx/grafico/venda_bilhete", views.grafico_venda_bilhete, name="grafico_venda_bilhete"),

    path("bilhetes/", BilheteList.as_view(), name="bilhete_list"),
    path("adicionar_bilhete/", views.adicionar_bilhete, name="adicionar_bilhete"),
]