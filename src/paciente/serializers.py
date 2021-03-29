from .models import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Paciente
        fields = ['nome', 'data_nascimento', 'genero', 'regiao', 'situacao', 'descricao']
