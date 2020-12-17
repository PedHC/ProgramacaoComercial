from django.test import TestCase
from cabeleleiros.models import *
from cabeleleiros.forms import *
from datetime import datetime,timedelta
from django.urls import reverse

# Create your tests here.
class TesteViewHorarioList(TestCase):

    def setUp(self): 
        self.url = reverse('lista_horario')
        cliente = Cliente.objects.create(nome='Paula Duarte',cpf='54689575215',data_criacao=datetime.now()) 
        servico = Servico.objects.create(descricao='Alisamento',duracao=1,preco=13.00)
        cabeleleiro = Cabeleleiro.objects.create(nome='Alessandra Nogueira',cpf='12564589785')
        Horario.objects.create(idCliente=cliente, idServico=servico,idCabeleleiro=cabeleleiro, horaInicio=datetime.now(),horaFim=datetime.now()+timedelta(hours=1))
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
        cliente = Cliente.objects.create(nome= 'Joao',cpf= '15468957885',data_criacao=datetime.now())
        servico = Servico.objects.create(descricao='Manicure',duracao= 4,preco= 20.0)
        cabeleleiro = Cabeleleiro.objects.create(nome='Lucelia Santos',cpf='15975385246')

        data = {
                'idCliente': cliente.pk, 
                'idServico': servico.pk, 
                'idCabeleleiro': cabeleleiro.pk, 
                'horaInicio': '12/12/2020 09:00:00', 
                'horaFim': '12/12/2020 11:00:00',
                'hora': '09:00', 
                'data': '12/12/2020',
            }
        response = self.client.post(self.url, data)
        
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('lista_horario'))

        self.assertEqual(Horario.objects.count(),1)
        self.assertEqual(Horario.objects.first().idCliente.nome, 'Joao')

class TesteViewHorarioEdit(TestCase):
    
    def setUp(self): 
        cliente = Cliente.objects.create(nome='Maria',cpf='15975385246',data_criacao=datetime.now())
        servico = Servico.objects.create(descricao='Escova',duracao=1,preco=20.0)
        cabeleleiro = Cabeleleiro.objects.create(nome='Joana',cpf='15478963515')
        self.instance = Horario.objects.create(idCliente = cliente, idServico= servico, idCabeleleiro= cabeleleiro,horaInicio=datetime.now(),horaFim=datetime.now())
        self.url = reverse('editar_horario', kwargs={'pk': self.instance.pk})
       
    
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Horario)
        self.assertIsInstance(response.context.get('form'), FormularioHorarioEdit)
        self.assertEqual(response.context.get('object').pk, self.instance.pk)
        self.assertEqual(response.context.get('object').idServico.preco, 20.0)
    def test_post(self):
        cliente = Cliente.objects.create(nome='Mariana',cpf='15975385246',data_criacao=datetime.now())
        servico = Servico.objects.create(descricao='Chapinha',duracao=1,preco=20.0)
        cabeleleiro = Cabeleleiro.objects.create(nome='Joana',cpf='15478963515')
        data = {
                'idCliente': cliente.pk, 
                'idServico': servico.pk, 
                'idCabeleleiro': cabeleleiro.pk, 
                'horaInicio': '12/12/2030 09:00:00', 
                'horaFim': '12/12/2030 11:00:00',
            }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_horario'))
        self.assertEqual(Horario.objects.count(), 1)
        self.assertEqual(Horario.objects.first().idCliente.nome, 'Mariana')
        self.assertEqual(Horario.objects.first().pk, self.instance.pk)

class TesteViewHorarioDelete(TestCase):
    
    def setUp(self):
        cliente = Cliente.objects.create(nome='Maria',cpf='15975385246',data_criacao=datetime.now()) 
        servico= Servico.objects.create(descricao='Escova',duracao=1,preco=20.0) 
        cabeleleiro= Cabeleleiro.objects.create(nome='Joana',cpf='15478963515')
        self.instance = Horario.objects.create(idCliente =cliente ,idServico = servico, idCabeleleiro= cabeleleiro ,horaInicio=datetime.now(),horaFim=datetime.now())
        self.url = reverse('cancelar_horario', kwargs={'pk': self.instance.pk})
       
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Horario)
        self.assertEqual(response.context.get('object').pk, self.instance.pk)

    
        
    def test_post(self):
        response = self.client.post(self.url)

        # Verifica se apos a exclusao houve um redirecionamento para a view VeiculosList
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_horario'))
        self.assertEqual(Horario.objects.count(), 0)

class TesteModeHorario(TestCase):

    def setUp(self):
        cliente = Cliente.objects.create(nome='Nayara Rodrigues',cpf='15975385246',data_criacao=datetime.now())
        servico= Servico.objects.create(descricao='Manicure',duracao=1,preco=20.0) 
        cabeleleiro= Cabeleleiro.objects.create(nome='Mariana',cpf='15478963515')
        self.instance = Horario(idCliente = cliente, idServico= servico, idCabeleleiro=cabeleleiro, horaInicio=datetime.now(),horaFim=datetime.now())

    def test_is_new(self):
        self.assertTrue(self.instance.expirado)
        self.instance.horaInicio = datetime.now()+timedelta(days=10)
        self.assertFalse(self.instance.expirado)
