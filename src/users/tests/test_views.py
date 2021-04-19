
from rest_framework.test import force_authenticate
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
        self.factory = APIRequestFactory()


    def test_create_psicologo(self):
        # changing zip code to create a unique property
        self.data = {
            "user": {
                "username": "afonso",
                "email": "afonso@solano.com",
                "password": "afonso_mg123"
            },
            "nCRP": "12345678912", # valid CPF
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
            "nCRP": "1", # valid CPF
            "bio": "Sou o afonso solano",
            "genero": "M"
        }
        request = self.factory.post(self.url_list, self.data, format='json')
        # force_authenticate(request, user=self.user) # TODO
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
