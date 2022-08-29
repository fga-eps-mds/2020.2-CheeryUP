from http import client
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from paciente.models import Consulta, Paciente
from users.models import Psicologo

class GraphEvolutionTestCase(APITestCase):
    def create_authentication_tokens(self, user_credentials):
        url_token = reverse('users:token_obtain_pair')

        response = self.client.post(
            url_token,
            user_credentials,
            format='json'
        )
        self.factory = APIRequestFactory()

        self.credentials = {
            'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']
        }

    def create_user(self):
        user_data = {
            "user": {
                "username": "lebronjames",
                "email": "lebron@example.com",
                "password": "adminadmin123"
            },
            "nCRP": "12345678912",
            "bio": "string",
            "genero": "M",
            "name": "lebron"
        }

        url_user_signup = reverse('psicologo-list')

        response = self.client.post(
            url_user_signup,
            user_data,
            format='json'
        )

        credentials = {
            "username": "lebronjames",
            "password": "adminadmin123",
        }

        self.create_authentication_tokens(credentials)
        return Psicologo.objects.first()

    def create_paciente(self):
        paciente = Paciente.objects.create(
            nome="anthony davis",
            cpf="11122233311",
            data_nascimento="2002-05-10",
            genero="M",
            regiao="EO",
            situacao="C",
            descricao="Jogou muito ontem",
            psicologo=self.create_user()
        )
        
    def create_consulta(self):
        self.create_paciente()
        self.url_list = reverse(
            'consultas-list',
            kwargs={'psicologo_user__username': 'lebronjames', 'paciente_cpf':'11122233311'}
        )
        self.credentials = {
            "username": "lebronjames",
            "'password": "adminadmin123",
        }
        self.consulta_data = {
            "produtividade": 1,
            "problemasPessoais": -1,
            "humor": -1,
            "estabilidadeDeEmoções": -1,
            "interessePelaVida": -1,
            "capacidadeDeSituaçõesDificeis": -1,
            "convivioFamiliar": -1,
            "energiaSono": -1,
            "convivioAmigos": -1,
            "conhecimentoDoenca": -1,
            "criseEspaçoInterior": -1,
            "exposiçãoRisco": -1,
            "qualidadeSono": -1,
            "tentativaSuicidio": -1,
            "qualidadeEscuta": -1,
            "maturidadeEmocional": -1,
            "qualidadeNutritiva": -1,
            "autoMedicacao": -1,
            "intoleranciaFrustração": -1
        }
        self.client.post(
            path=self.url_list,
            data=self.consulta_data,
            format='json',
            **self.credentials,
        )


    def testPacient(self):

        self.create_consulta()
        expexted = '{"consultas": [-22]}'

        self.get_graph_evolution = reverse(
            'get_graph_evolution',
            kwargs={
                'user__username': 'lebronjames', 
                'cpf':'11122233311'
            }
        )

        response = self.client.get(self.get_graph_evolution)


        self.assertEqual(expexted,  str(response.content ,encoding='utf8'))

    def test_exists_paciente(self):
        self.create_consulta()
        cpf = 11122233313
        expected = '{"error": "paciente não cadastrado"}'
        self.get_graph_evolution = reverse(
            'get_graph_evolution',
            kwargs={
                'user__username': 'lebronjames', 
                'cpf':f'{cpf}'
            }
        )

        response = self.client.get(self.get_graph_evolution)
        self.assertEqual(expected,  str(response.content, encoding='utf8')) 
class GetGenderTestCase(APITestCase):
    
    def create_user(self):
        user_data = {
            "user": {
                "username": "lebronjames",
                "email": "lebron@example.com",
                "password": "adminadmin123"
            },
            "nCRP": "12345678912",
            "bio": "string",
            "genero": "M",
            "name": "lebron"
        }
        url_user_signup = reverse('psicologo-list')

        response = self.client.post(
            url_user_signup,
            user_data,
            format='json'
        )
        return Psicologo.objects.first()

    def testPacient(self):
        psicologo = self.create_user()
        paciente = Paciente.objects.create(
            nome="anthony davis",
            cpf="9876543212",
            data_nascimento="2002-05-10",
            genero="M",
            regiao="EO",
            situacao="C",
            descricao="Jogou muito ontem",
            psicologo=psicologo
        )
        self.get_gender = reverse(
            'get_gender',
            kwargs={
                'user__username': 'lebronjames', 
            }
        )
        expected = '{"masculino": 1, "feminino": 0, "nIdentificado": 0}'             
        response = self.client.get(self.get_gender)
        self.assertEqual(response.status_code, 200 )
        self.assertEqual( str(response.content, encoding='utf8'), expected)

