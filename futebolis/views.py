from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores = [
        {"nome": "Leo Jardim", "idade": "29", "posicao": "Goleiro", "nascimento": "Ribeirao Preto(SP), Brazil", "foto": "img/Leo-J.png"},
        {"nome": "Puma Rodriguez", "idade": "27", "posicao": "Lateral D./Zagueiro", "nascimento": "Canelones, Uruguai", "foto": "img/Puma.png"},
        {"nome": "Maicon", "idade": "35", "posicao": "Zagueiro", "nascimento": "Barretos, Brazil", "foto": "img/Maicon.png"},
        {"nome": "Luiz Gustavo", "idade": "28", "posicao": "Zagueiro", "nascimento": "Rio de Janeiro, Brazil", "foto": "img/Luiz-Gustavo.png"},
        {"nome": "Lucas Piton", "idade": "23", "posicao": "Lateral Esquerdo", "nascimento": "Jundiaí, Brazil", "foto": "img/Piton.png"},
        {"nome": "Juan Sforza", "idade": "20", "posicao": "Meio Campista", "nascimento": "Rosario, Argentina", "foto": "img/Sforza.png"},
        {"nome": "Coutinho", "idade": "32", "posicao": "Meio Campista", "nascimento": "Rio de Janeiro, Brazil", "foto": "img/coutinho.png"},
        {"nome": "Guilherme Estrellas", "idade": "19", "posicao": "Meio Campista", "nascimento": "Rio de Janeiro, Brazil", "foto": "img/Estrella.png"},
        {"nome": "Emerson Rodriguez", "idade": "30", "posicao": "Atacante", "nascimento": "Colombia", "foto": "img/Emerson-Rodriguez-2.png"},
        {"nome": "Clayton", "idade": "25", "posicao": "Centroavante", "nascimento": "Belo Horizonte, Brazil", "foto": "img/Clayton.png"},
        {"nome": "Vegetti", "idade": "35", "posicao": "Atacante", "nascimento": "Santo Domingo, Argentina", "foto": "img/Vegetti.png"},
]

    context = {
        "jogadores": jogadores,
    }
    
    return render(request, "jogadores.html", context)
def sobre(request):
    return render(request, "sobre.html")