from django.db import models

class Reserva(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    pessoas = models.IntegerField()
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.nome} - {self.data} {self.horario}"