from .views import PacienteViewSet, ProductorRegistrationAPIView, PacienteDelete, PacienteUpdate
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'paciente', PacienteViewSet)
router.register(r'create', ProductorRegistrationAPIView)
router.register(r'delete', PacienteDelete)
router.register(r'update', PacienteUpdate)

