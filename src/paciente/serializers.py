from .models import Paciente
from rest_framework import serializers
from .models import Consulta
class PacienteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Paciente
        fields = ['nome', 'cpf', 'data_nascimento', 'genero', 'regiao',
                  'situacao', 'descricao']

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('numero de caracteres invalido')

        return cpf

class ConsultaSerializer(serializers.ModelSerializer):

    class Meta():
        model = Consulta
        fields = ['nome', 'registro','problemas']
