from django.core.checks.messages import Error
from django.shortcuts import render
from rest_framework import viewsets
from .models import Psicologo
from django.contrib.auth.models import User
from .serializers import PsicologoSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions



class PsicologoViewSet(viewsets.ModelViewSet):
    queryset = Psicologo.objects.all()
    serializer_class = PsicologoSerializer
    permission_classes = (permissions.AllowAny,)


    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)

    #     name = serializer.data.get('name').lower()
    #     email = serializer.data.get('email').lower()
    #     password = serializer.data.get('password')

    #     user = User.objects.create(username=name, email=email)
    #     user.set_password(password)
    #     serializer.is_valid(raise_exception=True) # descarta tudo model Psicologo
    #     self.perform_create(serializer, user)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    # def perform_create(self, serializer, user):
    #     Psicologo.objects.create(
    #         user=user,
    #         nCRP=serializer.data.get('nCRP'),
    #         bio=serializer.data.get('bio'),
    #         genero=serializer.data.get('genero')
    #     )


    # def get_success_headers(self, data):
    #     try:
    #         return {'Location': str(data[api_settings.URL_FIELD_NAME])}
    #     except (TypeError, KeyError):
    #         return {}
