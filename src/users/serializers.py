
from rest_framework import serializers
from .models import Psicologo
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
  
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
        # unique=True,
        label="Email Address",
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=6,
    )
 
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_password(self, password):
        if len(password) < 6:
            raise serializers.ValidationError('Senha fraca!')
            
        return password

class PsicologoSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Psicologo
        fields = ('user', 'nCRP', 'bio', 'genero')


    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        psicologo = Psicologo.objects.create(user=user, **validated_data)
        return psicologo

   

    def validate_nCRP(self, nCRP):
        if len(nCRP) != 11:
            raise serializers.ValidationError('numero de caracteres invalido')

        return nCRP