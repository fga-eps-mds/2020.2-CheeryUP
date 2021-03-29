
from rest_framework import serializers
from .models import Psicologo
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        # style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password')



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
        password = user_data.pop('password')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.set_password('password')
        psicologo = Psicologo.objects.create(user=user, **validated_data)
        return psicologo

