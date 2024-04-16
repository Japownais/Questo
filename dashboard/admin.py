from django.contrib import admin

from .models import Deck, Evento, Prova, Vestibular, Caderno, Correcao

# Register your models here.

admin.site.register(Deck)
admin.site.register(Evento)

admin.site.register(Prova)
admin.site.register(Vestibular)
admin.site.register(Caderno)
admin.site.register(Correcao)