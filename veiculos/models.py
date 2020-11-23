from django.db import models

# Create your models here.
class Veiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.IntegerField()
    modelo_fabricacao = models.IntegerField()
    
    valor = models.IntegerField(default=10000)
    
    combustivel = models.SmallIntegerField(choices=[(1,'ETANOl'),(2,'FLEX'),(3,'GASOLINA')])

    def __str__(self):
        return '{0} - {1} ({2}/{3}) {4}'.format(self.marca,self.modelo,self.ano_fabricacao,self.modelo_fabricacao, self.valor)