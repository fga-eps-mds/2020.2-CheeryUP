from rest_framework import routers

from users.models import Psicologo

# from .views import PacienteViewSet, PacienteRegistrationAPIView ,PacienteDelete, PacienteUpdate
from .views import PacienteModelViewSet


app_name = 'paciente'
router = routers.DefaultRouter()
router.register(r'paciente', PacienteModelViewSet)

# router.register(r'create', PacienteRegistrationAPIView)
# router.register(r'delete', PacienteDelete)
# router.register(r'update', PacienteUpdate)






