from django.core.checks.messages import Error
from django.shortcuts import render
from rest_framework import viewsets
from .models import Psicologo
from django.contrib.auth.models import User
from .serializers import PsicologoSerializer, ChangePasswordSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework import permissions, generics, mixins
from rest_framework.viewsets import GenericViewSet

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions



class PsicologoViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Psicologo.objects.all()
    serializer_class = PsicologoSerializer
    permission_classes = [AllowAny]



class PsicologoRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [AllowAny]

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


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint para alterar a senha
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Senha incorreta!"]})
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'Senha alterada!',
            }

            return Response(response)

        return Response(serializer.errors) 