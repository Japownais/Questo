from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DeckForm, EventoForm
from django.http import HttpResponse
from .models import Evento
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import json
from .models import Deck


# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def calendar(request):


    if request.method == 'POST':
        print("Com post")
        return data_calendar(request)
    else:
        print("Sem post")
        return render(request, 'calendar.html')

def data_calendar(request):
    if request.method == 'POST':
        dia_selecionado = int(request.POST.get('diaSelecionado'))
        mes_selecionado = int(request.POST.get('mesSelecionado')) + 1
        ano_selecionado = int(request.POST.get('anoSelecionado'))
        data = date(ano_selecionado, mes_selecionado, dia_selecionado)
        
        return JsonResponse({'data': data, 'dia': dia_selecionado, 'mes': mes_selecionado, 'ano': ano_selecionado})
  
    
def form_calendar(request):
    if request.method == 'POST':
        print("Botão apertado")
        return render(request, 'calendar.html')
    print("Botão não apertado ???")
    return render(request, 'calendar.html')


def home(request):
    return render(request,'home.html')

def flashcards(request):

    decks = Deck.objects.filter(usuario=request.user)  # Recupere os decks do usuário atual
    
    if request.method == 'POST':
        deck_form = DeckForm(request.POST)  # Inicialize o formulário com os dados submetidos
        if deck_form.is_valid():  # Verifique se o formulário é válido
            deck = deck_form.save(commit=False)  # Salve os dados do formulário sem commit no banco de dados
            deck.usuario = request.user  # Atribua o usuário atual ao deck
            deck.save()  # Salve o deck no banco de dados
            return HttpResponse("Deck salvo com sucesso!") 
    else:
        deck_form = DeckForm()  # Caso contrário, crie um formulário em branco para ser exibido
    
    # Renderize o template com o formulário e os decks do usuário atual
    return render(request, 'flashcards.html', {'decks': decks, 'deck_form': deck_form})