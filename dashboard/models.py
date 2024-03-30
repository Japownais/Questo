from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deck (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Flashcard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    pergunta = models.TextField()
    resposta = models.TextField()

    def __str__(self):
        return f"Flashcard: {self.pergunta}"
    

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.titulo