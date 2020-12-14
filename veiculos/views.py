from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from veiculos.models import Veiculo
from veiculos.forms import FormularioVeiculo
from django.http import HttpResponse
from django.urls import reverse_lazy
from sistema.utilitarios import AutenticacaoObrigatoria

class VeiculosList(ListView):
    model = Veiculo
    context_object_name = "lista_veiculos"
    template_name = "veiculos/listar.html"



class VeiculosNew(CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/novo.html'
    success_url = reverse_lazy('lista_veiculos')

class VeiculosEdit(UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculos/editar.html'
    success_url = reverse_lazy('lista_veiculos')

class VeiculosDelete(DeleteView):
    model = Veiculo
    template_name = 'veiculos/excluir.html'
    success_url = reverse_lazy('lista_veiculos')


from veiculos.serializers import SerializadorVeiculo
from rest_framework.generics import ListAPIView

class VeiculosListAPI(ListAPIView):
    serializer_class = SerializadorVeiculo

    def get_queryset(self):
        return Veiculo.objects.all()