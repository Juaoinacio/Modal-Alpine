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