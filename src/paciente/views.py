from rest_framework import viewsets
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

