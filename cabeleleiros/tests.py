from django.test import TestCase
from cabeleleiros.models import *
from cabeleleiros.forms import *
from datetime import datetime,timedelta
from django.urls import reverse

# Create your tests here.
class TesteViewHorarioList(TestCase):

    def setUp(self): 
        self.url = reverse('lista_horario') 
        Horario(
            Cliente('Paula Duarte','54689575215',datetime.now()),
            Servico('Alisamento',1,13.00),
            Cabeleleiro('Alessandra Nogueira','12564589785'),
            datetime.now(),
            datetime.now()+timedelta(hours=1)
        )
    def test_get(self): 
            '''
            Testa o método GET da URL de listagem de veículos
            '''
            response = self.client.get(self.url) 
            self.assertEqual(response.status_code, 200) 
            self.assertEqual(len(response.context.get('lista_horario')), 1)

class TesteViewHorarioNew(TestCase):
    
    def setUp(self): 
        self.url = reverse('novo_horario')
       
    
    def test_get(self):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.context.get('form'), FormularioHorario)

    def test_post(self):
            data = {
                'idCliente': {
                    'nome': 'Joao',
                    'cpf': '15468957885',
                    'data_criacao':datetime.now(),
                }, 
                'idServico': {
                    'descricao':'Manicure',
                    'duracao': 4,
                    'preco': 20.0,
                }, 
                'idCabeleleiro': {
                    'nome':'Lucelia Santos',
                    'cpf': '15975385246',
                }, 
                'horaInicio': '12/12/2030 09:00:00', 
                'horaFim': '12/12/2030 11:00:00',
            }
            response = self.client.post(self.url, data)
            
            self.assertEqual(response.status_code,302)
            self.assertRedirects(response,reverse('lista_horario'))

            self.assertEqual(Veiculo.objects.count(),1)
            self.assertEqual(Veiculo.objects.first().idCliente.nome, 'Joao')

class TesteViewHorarioEdit(TestCase):
    
    def setUp(self): 
        self.instance = Horario.objects.create(idCliente = Cliente('Jhonas','15975385246',datetime.now()), idServico= Servico('Escova',1,20.0), idCabeleleiro= Cabeleleiro('Joana','15478963515'),datetime.now(),datetime.now())
        self.url = reverse('editar_horario', kwargs={'pk': self.instance.pk})
       
    
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Horario)
        self.assertIsInstance(response.context.get('form'), FormularioHorarioEdit)
        self.assertEqual(response.context.get('object').pk, self.instance.pk)
        self.assertEqual(response.context.get('object').idServico.preco, 20.0)
    def test_post(self):
        data = {
                'idCliente': {
                    'nome': 'Joao',
                    'cpf': '15468957885',
                    'data_criacao':datetime.now(),
                }, 
                'idServico': {
                    'descricao':'Manicure',
                    'duracao': 4,
                    'preco': 20.0,
                }, 
                'idCabeleleiro': {
                    'nome':'Lucelia Santos',
                    'cpf': '15975385246',
                }, 
                'horaInicio': '12/12/2030 09:00:00', 
                'horaFim': '12/12/2030 11:00:00',
            }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_horario'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().idCliente.nome, 'Joao')
        self.assertEqual(Veiculo.objects.first().pk, self.instance.pk)

class TesteViewHorarioDelete(TestCase):
    
    def setUp(self): 
        self.instance = Veiculo.objects.create(marca='aaa', modelo='aaa', ano_fabricacao=1, modelo_fabricacao=2, combustivel=3, valor=15000)
        self.url = reverse('deletar_veiculo', kwargs={'pk': self.instance.pk})
       
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertEqual(response.context.get('object').pk, self.instance.pk)

    
        
    def test_post(self):
        response = self.client.post(self.url)

        # Verifica se apos a exclusao houve um redirecionamento para a view VeiculosList
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_veiculos'))
        self.assertEqual(Veiculo.objects.count(), 0)

class TesteModelVeiculos(TestCase):

    def setUp(self):
        self.instance = Veiculo(marca='aaa', modelo='aaa', ano_fabricacao = datetime.now().year, modelo_fabricacao=2, combustivel=3, valor=15000)

    def test_is_new(self):
        self.assertTrue(self.instance.veiculo_novo)
        self.instance.ano_fabricacao = datetime.now().year - 5
        self.assertFalse(self.instance.veiculo_novo)

    def test_years_use(self):
        self.assertEqual(self.instance.anos_de_uso, 0)
        self.instance.ano_fabricacao = datetime.now().year - 5
        self.assertEqual(self.instance.anos_de_uso, 5)