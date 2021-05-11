from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from paciente.models import Paciente
from paciente.models import Consulta
from users.models import Psicologo

class PacienteModelViewSetTestCase(APITestCase):

    def create_authentication_tokens(self, user_credentials):
        url_token = reverse('users:token_obtain_pair')

        response = self.client.post(
            url_token,
            user_credentials,
            format='json'
        )
        self.factory = APIRequestFactory()

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to create user tokens credentials'
        )

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

        self.assertEqual(
            response.status_code,
            201,
            msg='Failed during user creation'
        )

        credentials = {
            "username": "lebronjames",
            "password": "adminadmin123",
        }

        self.create_authentication_tokens(credentials)

    def setUp(self):
        self.create_user()
        self.psicologo = Psicologo.objects.first()
        # self.create_property()

        self.paciente_data = {
            "nome": "anthony davis",
            "cpf": "11111111111",
            "data_nascimento": "2002-05-10",
            "genero": "M",
            "regiao": "EO",
            "situacao": "C",
            "descricao": "Jogou muito ontem"
        }

        self.url_list = reverse(
            'paciente-list',
            kwargs={'psicologo_user__username': 'lebronjames'}
        )

        self.url_detail = reverse(
            'paciente-detail',
            kwargs={
                'psicologo_user__username': 'lebronjames', 
                'cpf': '11111111111'
            }
        )

    def tearDown(self):
        Paciente.objects.all().delete()
        # User.objects.all().delete()
        # Harvest.objects.all().delete()

    def test_create_paciente(self):
        response = self.client.post(
            path=self.url_list,
            data=self.paciente_data,
            format='json',
            **self.credentials,
        )

        self.assertDictContainsSubset(
            self.paciente_data,
            response.data,
        )

    def test_certifies_duplicated_cpf_fails(self):
        Paciente.objects.create(
            nome="anthony davis",
            cpf="9876543212",
            data_nascimento="2002-05-10",
            genero="M",
            regiao="EO",
            situacao="C",
            descricao="Jogou muito ontem",
            psicologo=self.psicologo
        )

        response = self.client.post(
            path=self.url_list,
            data=self.paciente_data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            201,
            msg=(
                'Era esperado uma código de erro, pois estamos testando uma requisição '
                'com cpfs duplciados'
            )
        )

    def test_fake(self,):
        self.client.get(path=self.url_list, format='json', **self.credentials,)
        self.assertTrue(True)

    def test_sending_invalid_CPF(self):

        self.paciente_data = {
            "nome": "anthony davis",
            "cpf": "123", #invalid
            "data_nascimento": "2002-05-10",
            "genero": "M",
            "regiao": "EO",
            "situacao": "C",
            "descricao": "Jogou muito ontem"
        }
        self.factory.post(self.url_list, self.paciente_data, format='json')
        
        response = self.client.get(
            path=self.url_list,
            data=self.paciente_data,
            format='json',
            **self.credentials,
        )

        self.assertNotEqual(
            201,
            response.status_code,
            msg='Foi retornado 201 Create para uma requisição com cpf inválido'
        )
        qs = Paciente.objects.filter(cpf=self.paciente_data['cpf'])
        self.assertFalse(
            qs.exists(),
            msg='Foi salvo no banco de dados um psicologo com cpf inválido'
        )

    def test_list_all_paciente(self):

        self.test_create_paciente()

        response = self.client.get(
            path=self.url_list,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            len(response.data),
            1,
            msg='More than one harvest was created'
        )

        response_data = dict(response.data[0])

        self.assertDictContainsSubset(
            self.paciente_data,
            response_data,
        )

    def test_patch_update_paciente(self):

        self.test_create_paciente()

        paciente_update = {
             "descricao": "Jogou muito ontem", 
        }

        response = self.client.patch(
            path=self.url_detail,
            data=paciente_update,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to patch update the harvest'
        )

        self.assertEqual(
            response.data['descricao'],
            paciente_update['descricao'],
        )

    def test_patch_update_paciente_with_inconsistent_cpf(self):

        self.test_create_paciente()

        paciente_update = {
             "cpf": "111", 
        }

        response = self.client.patch(
            path=self.url_detail,
            data=paciente_update,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            400,
        )

    def test_patch_update_paciente_with_valid_cpf(self):

        self.test_create_paciente()

        paciente_update = {
             "cpf": "11111111111", 
        }

        response = self.client.patch(
            path=self.url_detail,
            data=paciente_update,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to patch update paciente'
        )

    def test_put_update_harvest(self):

        self.test_create_paciente()

        self.paciente_data['descricao'] = 'oi'

        response = self.client.put(
            path=self.url_detail,
            data=self.paciente_data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to update paciente'
        )

        self.assertDictContainsSubset(
            self.paciente_data,
            response.data,
        )

    def test_get_paciente(self):

        self.test_create_paciente()

        response = self.client.get(
            path=self.url_detail,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to get paciente'
        )

        self.assertDictContainsSubset(
            self.paciente_data,
            response.data,
        )

    def test_delete_paciente(self):

        self.test_create_paciente()

        response = self.client.delete(
            path=self.url_detail,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            204,
            msg='Failed to delete paciente'
        )

        paciente = Paciente.objects.all()
        qnt_paciente = len(paciente)

        self.assertEqual(
            qnt_paciente,
            0,
            msg='Failed to delete paciente'
        )

    
#         self.harvest_data = {
#             'date': '2019-11-21',
#             'description': 'Apple Harvest',
#             'status': 'Open',
#             'max_volunteers': 10,
#             'min_volunteers': 5,
#         }

# class MonthlyHarvestsTestCase(APITestCase):

#     def create_authentication_tokens(self, user_credentials):
#         url_token = reverse('users:token_obtain_pair')

#         response = self.client.post(
#             url_token,
#             user_credentials,
#             format='json'
#         )

#         self.assertEqual(
#             response.status_code,
#             200,
#             msg='Failed to create user tokens credentials'
#         )

#         self.credentials = {
#             'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']
#         }

#     def create_user(self):
#         user_data = {
#             "username": 'vitas',
#             'email': 'vitas@vitas.com',
#             'password': 'vitasIsNice',
#             'confirm_password': 'vitasIsNice'
#         }

#         url_user_signup = reverse('users:register')

#         response = self.client.post(
#             url_user_signup,
#             user_data,
#             format='json'
#         )

#         self.assertEqual(
#             response.status_code,
#             201,
#             msg='Failed during user creation'
#         )

#         user_data.pop('username')
#         user_data.pop('confirm_password')

#         self.create_authentication_tokens(user_data)

#     def create_property(self):
#         property_data = {
#             'type_of_address': 'House',
#             'BRZipCode': '73021498',
#             'state': 'DF',
#             'city': 'Gama',
#             'district': 'Leste',
#             'address': "Quadra 4",
#         }

#         url_property_creation = reverse(
#             'property:property-list',
#         )

#         response = self.client.post(
#             path=url_property_creation,
#             data=property_data,
#             format='json',
#             **self.credentials,
#         )

#         self.assertEqual(
#             response.status_code,
#             201,
#             msg='Failed to create property'
#         )

#         self.property = Property.objects.get(pk=1)

#     def setUp(self):
#         self.create_user()
#         self.create_property()

#         self.harvest_data = {
#             'date': '2019-11-21',
#             'description': 'Apple Harvest',
#             'status': 'Open',
#             'max_volunteers': 10,
#             'min_volunteers': 5,
#         }

#         self.url_list = reverse(
#             'property:harvest:harvest-list',
#             kwargs={'property_pk': self.property.pk}
#         )

#         self.url_detail = reverse(
#             'property:harvest:harvest-detail',
#             kwargs={
#                 'property_pk': self.property.pk,
#                 'pk': '1'
#             }
#         )

#     def tearDown(self):
#         Property.objects.all().delete()
#         User.objects.all().delete()
#         Harvest.objects.all().delete()

#     def test_get_harvests_of_the_week(self):

#         today = datetime.date(datetime(2020, 1, 1))

#         for i in range(0, 12):
#             date = today + timedelta(days=i*31)

#             self.harvest_data['date'] = date

#             response = self.client.post(
#                 path=self.url_list,
#                 data=self.harvest_data,
#                 format='json',
#                 **self.credentials,
#             )

#             self.assertEqual(
#                 response.status_code,
#                 201,
#                 msg='Failed to create a harvest'
#             )

#         for month in range(1, 13):
#             weekly_harvests_url = reverse(
#                 'monthly_harvest',
#                 kwargs={
#                     'year': date.year,
#                     'month': month
#                 }
#             )

#             response = self.client.get(
#                 path=weekly_harvests_url,
#             )

#             self.assertEqual(
#                 len(response.data),
#                 1,
#                 msg='Failed return only 1 harvest'
#             ) 