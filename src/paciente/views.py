from http.client import HTTPResponse
from xml.etree.ElementTree import SubElement
from rest_framework import viewsets, permissions
from users.models import Psicologo
from .models import Paciente
from .serializers import PacienteSerializer
from .models import Consulta
from django.http import JsonResponse
from .serializers import ConsultaSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

class PacienteModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'cpf'

    def get_psicologo(self):
        return Psicologo.objects.get(user__username=self.kwargs['psicologo_user__username'])

    def get_queryset(self):
        psicologo = self.get_psicologo()
        return Paciente.objects.filter(psicologo=psicologo)

    def perform_create(self, serializer):
        psicologo = self.get_psicologo()
        serializer.save(psicologo=psicologo)


class ConsultaModelViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    lookup_field = 'id'

    def get_psicologo(self):
        return Psicologo.objects.get(user__username=self.kwargs['psicologo_user__username'])

    def get_paciente(self):
        return Paciente.objects.get(cpf=self.kwargs['paciente_cpf'])

    def get_queryset(self):
        paciente = self.get_paciente()
        return Consulta.objects.filter(paciente=paciente)

    def perform_create(self, serializer):   
        paciente = self.get_paciente()
        serializer.save(paciente=paciente)



def getGender(request, user__username):
    psicologo = Psicologo.objects.get(user__username=user__username)
    pacientes = Paciente.objects.filter(psicologo=psicologo)
    masculino = pacientes.filter(genero='M').count()
    feminino = pacientes.filter(genero='F').count()
    nIdentificado = pacientes.filter(genero='P').count()
    return JsonResponse({'masculino': masculino, 'feminino': feminino, 'nIdentificado': nIdentificado})


def getPacienteGraphEvolution(request, user__username, cpf):
   
    psicologo = Psicologo.objects.get(user__username=user__username)
    try:
        paciente = Paciente.objects.get(psicologo=psicologo, cpf=cpf)
    except:
        return JsonResponse({"error": "paciente não cadastrado"},json_dumps_params={'ensure_ascii': False}, safe=False) 
    consultas = list(Consulta.objects.filter(paciente=paciente))
    data = []
    for consulta in consultas:
        serializer = ConsultaSerializer(consulta).data
        especialAttributes = (serializer["humor"]+serializer["estabilidadeDeEmoções"])*3
        del serializer["id"], serializer["data"], serializer["produtividade"], serializer["humor"], serializer["estabilidadeDeEmoções"]
        soma = especialAttributes + sum(serializer.values())
        data.append(soma)        
    return JsonResponse({'consultas':data},json_dumps_params={'ensure_ascii': False}, status=200)        
