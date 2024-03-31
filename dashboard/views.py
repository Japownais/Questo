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
        
    context = {'form': form}
    return render(request, 'calendar.html', context=context)



"""""
def calendar(request):
    form = EventoForm()
    context = {
        'form': form
    }
    
    if request.method == 'POST':
        print("Com post")
        return data_calendar(request)
        
    else:
        print("Sem post")
        return render(request, 'calendar.html', context=context)

def data_calendar(request):
    
    if request.method == 'POST':
        dia_selecionado = int(request.POST.get('diaSelecionado'))
        mes_selecionado = int(request.POST.get('mesSelecionado')) + 1
        ano_selecionado = int(request.POST.get('anoSelecionado'))

        data = date(ano_selecionado, mes_selecionado, dia_selecionado)

        form_calendar(request)
        
        return JsonResponse({'data': data, 'dia': dia_selecionado, 'mes': mes_selecionado, 'ano': ano_selecionado})
        
         
    
def form_calendar(request):
    if request.method == 'GET':
        print("Com get")
    return render(request, 'calendar.html')
"""


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