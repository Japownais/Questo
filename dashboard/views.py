from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import tests


# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def calendar(request):
    return render(request, 'calendar/calendar.html')

@login_required
def vestibulares(request):
    novo_vestibular = tests()
    novo_vestibular.nivel_vestibular = request.POST.get('nivel')
    novo_vestibular.nm_vestibular = request.POST.get('nome')
    novo_vestibular.ano_vestibular = request.POST.get('ano')
    novo_vestibular.url_vestibular = request.POST.get('urlv')
    novo_vestibular.url_gabarito = request.POST.get('urlg')
    novo_vestibular.save()
    return render(request, 'tests/tests.html')
