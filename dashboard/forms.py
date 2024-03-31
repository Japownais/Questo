from django import forms
from .models import Deck, Flashcard,Evento

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['nome', 'descricao']
        labels = {
            'nome': 'Nome do Deck',
            'descricao': 'Descrição do Deck',
        }

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['deck', 'pergunta', 'resposta']
        labels = {
            'deck': 'Deck',
            'pergunta': 'Pergunta',
            'resposta': 'Resposta',
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'hora']
        labels = {
            'titulo': 'Título do Evento',
            'descricao': 'Descrição do Evento',
            'hora': 'Hora do Evento',
        }


        