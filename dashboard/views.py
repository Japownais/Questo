from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DeckForm, EventoForm
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
from .models import Evento, Deck
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime
import json
from django.utils.html import format_html
from django.forms.models import model_to_dict

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
@csrf_exempt
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

    if request.method == 'POST':
        data_selecionada = request.POST.get('dataAtiva')
        data_selecionada = datetime.strptime(data_selecionada, '%Y-%m-%d').date()

        eventos = Evento.objects.filter(usuario=request.user, data=data_selecionada).order_by('hora')
        eventos_dict = [model_to_dict(evento) for evento in eventos]
        lista_data_evento = [evento.data.strftime('%Y-%m-%d') for evento in eventos]

        context = {'eventos': eventos_dict, 'lista_data_evento': lista_data_evento}
        return JsonResponse(context)
    else:
        form = EventoForm()
        eventos_marcados = Evento.objects.filter(usuario=request.user)
        datas_eventos = [evento.data for evento in eventos_marcados]
        lista_data_evento = [data.strftime('%Y-%m-%d') for data in datas_eventos]

        eventos = Evento.objects.filter(usuario=request.user, data=date(2024, 4, 30))

        context = {'form': form, 'datas_eventos': datas_eventos, 'lista_data_evento': lista_data_evento, 'eventos': eventos}
        return render(request, 'calendar.html', context=context)

def flashcards(request):
    decks = Deck.objects.filter(usuario=request.user)
    if request.method == 'POST':
        deck_form = DeckForm(request.POST)  # Inicialize o formulário com os dados submetidos
        if deck_form.is_valid():  # Verifique se o formulário é válido
            deck = deck_form.save(commit=False)  # Salve os dados do formulário sem commit no banco de dados
            deck.usuario = request.user  # Atribua o usuário atual ao deck
            deck.save()  # Salve o deck no banco de dados
            return redirect('flashcards')
    else:
        deck_form = DeckForm()  # Caso contrário, crie um formulário em branco para ser exibido
    
    # Renderize o template com o formulário e os decks do usuário atual
    return render(request, 'flashcards.html', {'decks': decks, 'deck_form': deck_form})

def deletar_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        deck.delete()
        return redirect('flashcards')
    return redirect('flashcards')

@login_required
def exams(request):
    return render(request, 'exams.html')