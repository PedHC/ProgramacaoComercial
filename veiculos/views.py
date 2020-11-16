from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic import ListView,CreateView
from veiculos.models import Veiculo
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.
class VeiculosList(ListView):
    model = Veiculo
    context_object_name = "lista_veiculos"
    template_name = "veiculos/listar.html"