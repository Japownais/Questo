from django.db import models

# Create your models here.

class tests (models.Model):
    nivel_vestibular = models.CharField(max_length=30)
    nm_vestibular = models.CharField(max_length=20)
    ano_vestibular = models.IntegerField()
    url_vestibular = models.TextField()
    url_gabarito = models.TextField()