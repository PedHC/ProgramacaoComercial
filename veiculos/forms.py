from django import forms
from veiculos.models import Veiculo

class FormularioVeiculo(forms.ModelForm):
    """
    Formulario para o model Veiculo
    """
    class Meta:
        model = Veiculo
        exclude = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class':'form-control'})