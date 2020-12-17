from rest_framework import serializers
from cabeleleiros.models import Horario,Cliente

class SerializadorHorario(serializers.ModelSerializer):
    
    class Meta:
        model = Horario
        exclude = []

class SerializadorCliente(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        exclude = []