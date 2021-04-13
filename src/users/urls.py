from .views import PsicologoViewSet,PsicologoRegistrationAPIView, PsicologoDelete, PsicologoUpdate
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()

router.register(r'psicologo/list', PsicologoViewSet)
router.register(r'psicologo/create', PsicologoRegistrationAPIView)
router.register(r'psicologo/delete', PsicologoDelete)
router.register(r'psicologo/update', PsicologoUpdate)

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]