from django.urls import path
from .views import form_calendar

urlpatterns = [
    path('form_calendar/', form_calendar, name='form_calendar'),
]