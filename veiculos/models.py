from django.db import models
from datetime import datetime

# Create your models here.


class Veiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.PositiveIntegerField(default=2000)
    modelo_fabricacao = models.PositiveIntegerField(default=2000)
    
    valor = models.PositiveIntegerField(default=10000)
    
    combustivel = models.SmallIntegerField(choices=[(1,'ETANOl'),(2,'FLEX'),(3,'GASOLINA')])

    def __str__(self):
        return '{0} - {1} ({2}/{3}) {4}'.format(self.marca,self.modelo,self.ano_fabricacao,self.modelo_fabricacao, self.valor)

    @property
    def veiculo_novo(self):
        return self.ano_fabricacao == datetime.now().year

    @property
    def anos_de_uso(self):
        return datetime.now().year - self.ano_fabricacao

