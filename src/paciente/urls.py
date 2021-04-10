from .views import PacienteViewSet, ProductorRegistrationAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'paciente', PacienteViewSet)
router.register(r'create', ProductorRegistrationAPIView)

