from django import forms
from cabeleleiros.models import Horario,Cliente,Cabeleleiro,Servico
from datetime import datetime, timedelta

class FormularioHorario(forms.ModelForm):
    """
    Formulario para o model Horario
    """
    class Meta:
        model = Horario
        exclude = ['horaFim']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['idCabeleleiro'].label = 'Cabeleleiro'
        self.fields['idCliente'].label = 'Cliente'
        self.fields['idServico'].label = 'Serviço'
        self.fields['horaInicio'].label = 'Data/Hora (dd/mm/aaaa 00:00)'
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class':'form-control'})
    '''
    def save(self, *args, **kwargd):
        self.fields['horaFim'] = self.fields['horaInicio'] + timedelta(hours=1)
        super().save(*args, **kwargs)
    '''
class FormularioCliente(forms.ModelForm):
    """
    Formulario para o model Horario
    """
    class Meta:
        model = Cliente
        exclude = ['data_criacao']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class':'form-control'})
    
    