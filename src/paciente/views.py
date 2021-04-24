from rest_framework import viewsets
from users.models import Psicologo
from .models import Paciente
from .serializers import PacienteSerializer


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
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'cpf'

    def get_psicologo(self):
        return Psicologo.objects.get(nCRP=self.kwargs['psicologo_nCRP'])

    def get_queryset(self):
        psicologo = self.get_psicologo()
        return Paciente.objects.filter(psicologo=psicologo)

    def perform_create(self, serializer):
        psicologo = self.get_psicologo()
        #paciente = serializer.save(psicologo=psicologo)
        serializer.save(psicologo=psicologo)
