# from .views import PsicologoViewSet,PsicologoRegistrationAPIView, PsicologoDelete, PsicologoUpdate
# from .views import PsicologoModelViewSet
from django.urls import path
from .views import CustomTokenObtainPairView
# from rest_framework_nested import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# psicologo_router = routers.DefaultRouter()
# psicologo_router.register(r'psicologos', PsicologoModelViewSet)

# router.register(r'psicologo/list', PsicologoViewSet)
# router.register(r'psicologo/create', PsicologoRegistrationAPIView)
# router.register(r'psicologo/delete', PsicologoDelete)
# router.register(r'psicologo/update', PsicologoUpdate)

urlpatterns = [
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
