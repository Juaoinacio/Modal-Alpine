from django.shortcuts import render

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
