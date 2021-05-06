from rest_framework import viewsets, permissions
from users.models import Psicologo
from .models import Paciente
from .serializers import PacienteSerializer
from .models import Consulta
from .serializers import ConsultaSerializer


# class PacienteViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):

#     queryset = Paciente.objects.all()
#     serializer_class = PacienteSerializer

# class PacienteRegistrationAPIView(GenericViewSet, mixins.CreateModelMixin):
#     serializer_class = PacienteSerializer
#     queryset = Paciente.objects.all()

# class PacienteDelete(GenericViewSet, mixins.DestroyModelMixin):

#     serializer_class = PacienteSerializer
#     queryset = Paciente.objects.all()
#     lookup_field = 'cpf'

# class PacienteUpdate(GenericViewSet, mixins.UpdateModelMixin):

#     serializer_class = PacienteSerializer
#     queryset = Paciente.objects.all()
#     lookup_field = 'cpf'

class PacienteModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
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
        # paciente = serializer.save(psicologo=psicologo)
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
        # paciente = serializer.save(psicologo=psicologo)
        serializer.save(paciente=paciente)
