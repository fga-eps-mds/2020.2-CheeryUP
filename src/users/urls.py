from .views import PsicologoViewSet,PsicologoRegistrationAPIView, PsicologoDelete, PsicologoUpdate
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'psicologo/list', PsicologoViewSet)
router.register(r'psicologo/create', PsicologoRegistrationAPIView)
router.register(r'psicologo/delete', PsicologoDelete)
router.register(r'psicologo/update', PsicologoUpdate)
