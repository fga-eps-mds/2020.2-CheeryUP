from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Psicologo
from .serializers import PsicologoSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions

# from rest_framework.decorators import permission_classes
# from django.core.checks.messages import Error
# from django.shortcuts import render
# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.settings import api_settings
# from rest_framework.viewsets import GenericViewSet
# from rest_framework import mixins, permissions
# class PsicologoViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
#     queryset = Psicologo.objects.all()
#     serializer_class = PsicologoSerializer
#     permission_classes = (permissions.IsAuthenticated,)
# class PsicologoRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
#     serializer_class = PsicologoSerializer
#     queryset = Psicologo.objects.all()
# class PsicologoDelete(GenericViewclass CustomTokenObtainPairView(TokenObtainPairView):
# Replace the serializer with your custom
#serializer_class = CustomTokenObtainPairSerializerSet, mixins.DestroyModelMixin):
#     serializer_class = PsicologoSerializer
#     queryset = Psicologo.objects.all()
#     lookup_field = 'nCRP'
# class PsicologoUpdate(GenericViewSet, mixins.UpdateModelMixin):
#     serializer_class = PsicologoSerializer
#     queryset = Psicologo.objects.all()
#     lookup_field = 'nCRP'

class PsicologoModelViewSet(viewsets.ModelViewSet):
    serializer_class = PsicologoSerializer
    queryset = Psicologo.objects.all()
    lookup_field = 'user__username'
    permission_classes = (permissions.AllowAny,)

    # @permission_classes([AllowAny])
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

class BlacklistTokenUpdateView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class= CustomTokenObtainPairSerializer
