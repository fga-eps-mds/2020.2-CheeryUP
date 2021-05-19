from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Psicologo
from .serializers import PsicologoSerializer, CustomTokenObtainPairSerializer
from rest_framework import permissions
class PsicologoModelViewSet(viewsets.ModelViewSet):
    serializer_class = PsicologoSerializer
    queryset = Psicologo.objects.all()
    lookup_field = 'user__username'
    permission_classes = (permissions.AllowAny,)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
