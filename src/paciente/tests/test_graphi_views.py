from http import client
from venv import create
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from paciente.models import Paciente
from users.models import Psicologo
from django.contrib.auth.models import User

class GraphEvolutionTestCase(APITestCase):
    
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

    def create_paciente(self):
        paciente = Paciente.objects.create(
            Paciente.objects.create(
            nome="anthony davis",
            cpf="9876543212",
            data_nascimento="2002-05-10",
            genero="M",
            regiao="EO",
            situacao="C",
            descricao="Jogou muito ontem",
            psicologo=self.create_user()
        )
        )
    def testPacient(self):
        paciente = self.create_paciente
        self.assertEqual( 1+1, 2)


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

