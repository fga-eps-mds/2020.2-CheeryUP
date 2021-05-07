from .models import Paciente
from rest_framework import serializers
from .models import Consulta

class PacienteSerializer(serializers.ModelSerializer):
    class Meta():
        model = Paciente
        fields = ['nome', 'cpf', 'data_nascimento', 'genero', 'regiao',
                  'situacao', 'descricao']

    def validate_number_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('CPF precisa possuir 11 digitos')

        return cpf

class ConsultaSerializer(serializers.ModelSerializer):

    class Meta():
        model = Consulta
        fields = [
            'id',
            'data',
            'produtividade',
            'problemasPessoais',
            'humor', 
            'estabilidadeDeEmoções',
            'interessePelaVida',
            'capacidadeDeSituaçõesDificeis',
            'convivioFamiliar',
            'energiaSono',
            'convivioAmigos',
            'conhecimentoDoenca',
            'criseEspaçoInterior',
            'exposiçãoRisco',
            'qualidadeSono',
            'tentativaSuicidio',
            'qualidadeEscuta',
            'maturidadeEmocional',
            'qualidadeNutritiva',
            'autoMedicacao',
            'intoleranciaFrustração',
            ]
