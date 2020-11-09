from django.shortcuts import render
from django.views.generic import View

class Autentificacao(View):
    def get(self,request):
        contexto = {
            'usuario':  '',
            'senha':    '',
            'mensagem': 'Programação Comercial'
        }
        return render(request,'autentificacao.html', contexto)