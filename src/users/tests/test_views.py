
# from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from users import views
from users.models import Psicologo

class PsicologoModelViewSetTestCase(APITestCase):

    def setUp(self):
        self.view_list = views.PsicologoModelViewSet.as_view({
            'post': 'create',
            'get': 'list',
        })
        self.url_list = reverse(
            'psicologo-list',
        )
        self.url_detail = reverse(
            'psicologo-detail', 
            kwargs={'user__username': 'afonso'} 

        )
        self.factory = APIRequestFactory()

    def test_create_psicologo(self):
        # changing zip code to create a unique property
        self.data = {
            "user": {
                "username": "afonso",
                "email": "afonso@solano.com",
                "password": "afonso_mg123"
            },
            "nCRP": "12345678912",   # valid CPF
            "bio": "Sou o afonso solano",
            "genero": "M"
        }
        request = self.factory.post(self.url_list, self.data, format='json')
        # force_authenticate(request, user=self.user) # TODO
        response = self.view_list(request)
        self.assertEqual(201, response.status_code)
        qs = Psicologo.objects.filter(nCRP=self.data['nCRP'])
        self.assertTrue(qs.exists())

    def test_sending_invalid_nCRP(self):
        # changing zip code to create a unique property
        self.data = {
            "user": {
                "username": "afonso",
                "email": "afonso@solano.com",
                "password": "afonso_mg123"
            },
            "nCRP": "1",  # invalid CPF
            "bio": "Sou o afonso solano",
            "genero": "M"
        }
        request = self.factory.post(self.url_list, self.data, format='json')
        # force_authenticate(request, user=self.user)  # TODO
        response = self.view_list(request)
        self.assertNotEqual(
            201,
            response.status_code,
            msg='Foi retornado 201 Create para uma requisição com nCRP inválido'
        )
        qs = Psicologo.objects.filter(nCRP=self.data['nCRP'])
        self.assertFalse(
            qs.exists(),
            msg='Foi salvo no banco de dados um psicologo com CRP inválido'
        )

    def test_unique_email_validation(self):
        """
        Test to try to create a user with
        a registered username
        """

        self.data = {
            "user": {
                "username": "afonso",
                "email": "afonso@solano.com",
                "password": "123456"
            },
            "nCRP": "11111111111",   # invalid CPF
            "bio": "Sou o afonso solano",
            "genero": "M"
        }

        request = self.factory.post(self.url_list, self.data, format='json')
        response = self.view_list(request)
        self.assertEqual(201, response.status_code)

        self.data = {
            "user": {
                "username": "afonso",
                "email": "afonso@solano.com",
                "password": "123456"
            },
            "nCRP": "111111111112", "bio": "Sou o afonso solano", "genero": "M"
        }
                
        request = self.factory.post(self.url_list, self.data, format='json')
        response = self.view_list(request)
        self.assertEqual(400, response.status_code)

    def test_delete_psicologo(self):

        self.test_create_psicologo()

        response = self.client.delete(
            path=self.url_detail,
            format='json',
        )

        self.assertEqual(
            response.status_code,
            204,
            msg='Failed to delete paciente'
        )

        psicologo = Psicologo.objects.all()
        qnt_psicologo = len(psicologo)

        self.assertEqual(
            qnt_psicologo,
            0,
            msg='Failed to delete psicologo'
        )

    def test_patch_update_psicologo(self):

        self.test_create_psicologo()

        psicologo_update = {
             "bio": "Oi, eu sou o Goku", 
        }

        response = self.client.patch(
            path=self.url_detail,
            data=psicologo_update,
            format='json',
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to patch update the psicologo'
        )

        self.assertEqual(
            response.data['bio'],
            psicologo_update['bio'],
        )

    def test_patch_update_psicologo_with_inconsistent_ncrp(self):

        self.test_create_psicologo()

        psicologo_update = {
             "nCRP": "111", 
        }

        response = self.client.patch(
            path=self.url_detail,
            data=psicologo_update,
            format='json',
        )

        self.assertEqual(
            response.status_code,
            400,
        )

    def test_patch_update_paciente_with_valid_cpf(self):

        self.test_create_psicologo()
        
        psicologo_update = {
             "nCRP": "11111111111", 
        }

        response = self.client.patch(
            path=self.url_detail,
            data=psicologo_update,
            format='json',
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to patch update psicologo'
        )

    def test_put_update_paciente(self):

        self.test_create_psicologo()

        self.data['bio'] = 'oi'

        response = self.client.put(
            path=self.url_detail,
            data=self.data,
            format='json',
        )

        self.assertEqual(
            response.status_code,
            400,
            msg='Failed to update psicologo'
        )

    def test_sending_invalid_password(self):
        # changing zip code to create a unique property
        self.data = {
            "user": {
                "username": "afonso",
                "email": "afonso@solano.com",
                "password": "123"   # invalid password
            },
            "nCRP": "12345678910", "bio": "Sou o afonso solano", "genero": "M"
        }
        request = self.factory.post(self.url_list, self.data, format='json')
        # force_authenticate(request, user=self.user) # TODO
        response = self.view_list(request)
        self.assertNotEqual(
            201,
            response.status_code,
            msg='Foi retornado 201 Create para uma requisição com senha inválido'
        )
        
class TOkenModelViewSet(APITestCase):

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

    def test_create_user(self):
        self.user_data = {
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
            self.user_data,
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
