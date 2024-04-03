from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DeckForm, EventoForm
from django.http import HttpResponse
from .models import Evento
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import json
from .models import Deck
from django.utils.html import format_html

# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def calendar(request):    
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario = request.user
            data_selecionada = request.POST.get('data')
            evento.data = data_selecionada
            evento.save()
            return redirect('calendar')
    else:
        form = EventoForm()

    eventos = Evento.objects.filter(usuario=request.user)  # Busca todos os eventos do banco de dados filtrando o usuario
    datas_eventos = [evento.data for evento in eventos]  # Lista de datas dos eventos

    lista_data_evento = []
    for data in datas_eventos:
        # Adiciona a tag 'event' a cada data na lista   
        data_formatada = format_html('{}', data)
        # Renderiza ou imprime a HTML   
        lista_data_evento.append(data_formatada)
    print(lista_data_evento)

    context = {'form': form, 'datas_eventos': datas_eventos, 'lista_data_evento': lista_data_evento}
    return render(request, 'calendar.html', context=context)

def home(request):
    return render(request,'home.html')

def flashcards(request):

    decks = Deck.objects.filter(usuario=request.user)



    if request.method == 'POST':
        deck_form = DeckForm(request.POST)  # Inicialize o formulário com os dados submetidos
        if deck_form.is_valid():  # Verifique se o formulário é válido
            Evento.usuario = request.user
            deck_form.save()  # Salve os dados do formulário no banco de dados
            return HttpResponse("Deck salvo com sucesso!") 
    else:
        deck_form = DeckForm()  # Caso contrário, crie um formulário em branco para ser exibido
    return render(request, 'flashcards.html', {'decks': decks})  # Renderize o template com o formulário