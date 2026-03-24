from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("htmx/bilhete/informacao", views.bilhete_informacao, name="informacao"),
    path("htmx/bilhete/informacao/detalhes", views.bilhete_informacao_detalhes, name="detalhes"),
]