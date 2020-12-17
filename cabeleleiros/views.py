from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from cabeleleiros.models import Horario,Cliente,Servico
from cabeleleiros.forms import FormularioHorario,FormularioCliente,FormularioHorarioEdit
from django.http import HttpResponse
from django.urls import reverse_lazy
from sistema.utilitarios import AutenticacaoObrigatoria
from datetime import datetime,timedelta
from django.forms import modelformset_factory


class HorarioList(ListView,AutenticacaoObrigatoria):
    model = Horario
    context_object_name = "lista_horario"
    template_name = "cabeleleiros/listar.html"


class HorarioNew(CreateView,AutenticacaoObrigatoria):
    model = Horario
    form_class = FormularioHorario
    template_name = 'cabeleleiros/novo.html'
    success_url = reverse_lazy('lista_horario')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.horaInicio = datetime.combine(datetime.strptime(form.data['data'],"%d/%m/%Y"),datetime.strptime(form.data['hora'],"%H:%M").time())
        self.object.horaFim = self.object.horaInicio + timedelta(hours=Servico.objects.get(pk=self.object.idServico.pk).duracao)
        
        return super(HorarioNew, self).form_valid(form)

class HorarioEdit(UpdateView,AutenticacaoObrigatoria):
    model = Horario
    form_class = FormularioHorarioEdit
    template_name = 'cabeleleiros/editar.html'
    success_url = reverse_lazy('lista_horario')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        #self.object.horaInicio = datetime.combine(datetime.strptime(form.data['data'],"%d/%m/%Y"),datetime.strptime(form.data['hora'],"%H:%M").time())
        self.object.horaFim = self.object.horaInicio + timedelta(hours=Servico.objects.get(pk=self.object.idServico.pk).duracao)
        
        return super(HorarioEdit, self).form_valid(form)

class HorarioDelete(DeleteView,AutenticacaoObrigatoria):
    model = Horario
    template_name = 'cabeleleiros/excluir.html'
    success_url = reverse_lazy('lista_horario')

class ClientesList(ListView,AutenticacaoObrigatoria):
    model = Cliente
    context_object_name = "lista_clientes"
    template_name = 'cabeleleiros/cliente/listar.html'

class ClientesNew(CreateView,AutenticacaoObrigatoria):
    model = Cliente
    form_class = FormularioCliente
    template_name = 'cabeleleiros/cliente/novo.html'
    success_url = reverse_lazy('lista_clientes')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.data_criacao = datetime.now()
        return super(ClientesNew, self).form_valid(form)

class ClienteEdit(UpdateView,AutenticacaoObrigatoria):
    model = Cliente
    form_class = FormularioCliente
    template_name = 'cabeleleiros/cliente/editar.html'
    success_url = reverse_lazy('lista_clientes')

class ClienteDelete(DeleteView,AutenticacaoObrigatoria):
    model = Cliente
    template_name = 'cabeleleiros/cliente/excluir.html'
    success_url = reverse_lazy('lista_clientes')

from cabeleleiros.serializers import SerializadorHorario,SerializadorCliente
from rest_framework.generics import ListAPIView

class HorarioListAPI(ListAPIView):
    serializer_class = SerializadorHorario

    def get_queryset(self):
        return Horario.objects.all()

class ClienteListAPI(ListAPIView):
    serializer_class = SerializadorCliente

    def get_queryset(self):
        return Cliente.objects.all()