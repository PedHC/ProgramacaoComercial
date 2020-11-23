from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic import ListView,CreateView
from veiculos.models import Veiculo
from veiculos.forms import FormularioVeiculo
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.
class VeiculosList(ListView):
    model = Veiculo
    context_object_name = "lista_veiculos"
    template_name = "veiculos/listar.html"

class VeiculosNew(CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/novo.html'
    success_url = reverse_lazy('lista_veiculos')
