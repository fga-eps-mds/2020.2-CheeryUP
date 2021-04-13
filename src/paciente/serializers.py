from .models import Paciente
from rest_framework import serializers
from users.serializers import PsicologoSerializer

class PacienteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Paciente
        fields = ['nome', 'cpf', 'data_nascimento', 'psicologo', 'genero', 'regiao', 'situacao', 'descricao']

