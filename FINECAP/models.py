from django.db import models

class Reserva(models.Model):
    cnpj = models.CharField(max_length=12)
    nome_empresa = models.CharField(max_length=150)
    categoria_empresa = models.CharField(max_length=50)
    quitado = models.BooleanField()

    def __str__(self):
        return self.nome_empresa

class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

