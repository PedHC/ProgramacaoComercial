from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=12)
    data_criacao = models.DateField()

    def __str__(self):
        return "{0}".format(self.nome)
class Servico(models.Model):
    descricao = models.CharField(max_length = 100)
    duracao = models.PositiveIntegerField()
    preco = models.FloatField()

    def __str__(self):
        return "{0}".format(self.descricao)

class Cabeleleiro(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    
    def __str__(self):
        return "{0}".format(self.nome)

class Horario(models.Model):
    idCliente = models.ForeignKey(Cliente,on_delete = models.CASCADE)
    idServico = models.ForeignKey(Servico,on_delete = models.CASCADE)
    idCabeleleiro = models.ForeignKey(Cabeleleiro,on_delete = models.CASCADE)
    horaInicio = models.DateTimeField()
    horaFim = models.DateTimeField()

    def __str__(self):
        nomeCabeleleiro = self.idCabeleleiro.nome
        nomeCliente = self.idCliente.nome
        servico = self.idServico.descricao
        return 'Horario: {0} {1} às {2} {3}  - Cliente: {4} - Cabeleleiro(a): {5} - Serviço: {6}'.format(self.horaInicio.date().strftime("%d/%m/%Y"),self.horaInicio.time().strftime("%H:%M"),self.horaFim.date().strftime("%d/%m/%Y"),self.horaFim.time().strftime("%H:%M"),nomeCliente,nomeCabeleleiro,servico)
'''
    @permalink
    def get_absolute_url(self):
        return ('myurlname', (), {'myparam': something_useful})
'''


    