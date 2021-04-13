from .views import PacienteViewSet, PacienteRegistrationAPIView, PacienteDelete, PacienteUpdate
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'paciente', PacienteViewSet)
router.register(r'create', PacienteRegistrationAPIView)
router.register(r'delete', PacienteDelete)
router.register(r'update', PacienteUpdate)

