from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView

from .models import Bilhete

def dashboard(request):
    return render(request, 'dashboard.html')

def bilhete_informacao(request):

    context = {
        "title": "Bilhete Informacao",
    }

    return render(request, "partials/bilhete_informacao.html", context)

def bilhete_informacao_detalhes(request):
    return render(request, "partials/bilhete_informacao_detalhes.html")

def grafico_venda_bilhete(request):
    data = {
        "renderTo": "grafico-coluna",
        "type": "line",
        "title": "Vendas de Bilhetes",
        "categories": ['Jan', 'Fev', 'Mar', 'Abr'],
        "serie": [
            {"name": "Vendas", "data": [10, 15, 20, 25]}
        ]
    }

    # Renderiza diretamente o template do gráfico (JS)
    return render(request, "components/column_chart.html", {'data': data})


# VOU VER COMO FAZER UMA VBC
class BilheteList(ListView):
    template_name = "bilhetes.html"
    model = Bilhete
    context_object_name = "bilhetes"

    def get_queryset(self):
        print(Bilhete.objects.all())
        return Bilhete.objects.all()


def adicionar_bilhete(request):
    titulo = request.POST.get("titulo")

    if Bilhete.objects.filter(name=titulo).exists():
        messages.error(request, "Já existe um bilhete com esse nome!")
    else:
        Bilhete.objects.create(name=titulo)
        messages.success(request, "Bilhete criado com sucesso!")

    bilhetes = Bilhete.objects.all()


    return render(request, "partials/bilhete-list.html", {
        "bilhetes": bilhetes
    })