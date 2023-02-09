from django.db import models
from atracoes.models import Local


# Create your models here.

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    local = models.ManyToManyField(Local)

    def __str__(self):
        return self.nome
