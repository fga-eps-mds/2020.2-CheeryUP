from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from .models import Paciente
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from rest_framework.decorators import api_view, permission_classes
from .serializers import PacienteSerializer


class PacienteViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()


class PacienteRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()


class PacienteDelete(GenericViewSet, mixins.DestroyModelMixin):

    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()
    lookup_field = 'cpf'

class PacienteUpdate(GenericViewSet, mixins.UpdateModelMixin):

    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()
    lookup_field = 'cpf'

