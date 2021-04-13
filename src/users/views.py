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



class PsicologoViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Psicologo.objects.all()
    serializer_class = PsicologoSerializer
    permission_classes = (permissions.IsAuthenticated,)



class PsicologoRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):

    serializer_class = PsicologoSerializer
    queryset = Psicologo.objects.all()


class PsicologoDelete(GenericViewSet, mixins.DestroyModelMixin):
    serializer_class = PsicologoSerializer
    queryset = Psicologo.objects.all()
    lookup_field = 'nCRP'


class PsicologoUpdate(GenericViewSet, mixins.UpdateModelMixin):
    serializer_class = PsicologoSerializer
    queryset = Psicologo.objects.all()
    lookup_field = 'nCRP'

