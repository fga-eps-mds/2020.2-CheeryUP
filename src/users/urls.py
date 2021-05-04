# from .views import PsicologoViewSet,PsicologoRegistrationAPIView, PsicologoDelete, PsicologoUpdate
# from .views import PsicologoModelViewSet
from django.urls import path
from .views import BlacklistTokenUpdateView, PsicologoModelViewSet

# from rest_framework_nested import routers


# psicologo_router = routers.DefaultRouter()
# psicologo_router.register(r'psicologos', PsicologoModelViewSet)

# router.register(r'psicologo/list', PsicologoViewSet)
# router.register(r'psicologo/create', PsicologoRegistrationAPIView)
# router.register(r'psicologo/delete', PsicologoDelete)
# router.register(r'psicologo/update', PsicologoUpdate)

urlpatterns = [
    
    path('blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]