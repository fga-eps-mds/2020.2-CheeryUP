from django.contrib import admin
from django.urls import path, include
# from paciente.views import PacienteViewSet
from rest_framework_nested import routers
from rest_framework.authtoken.views import obtain_auth_token

from users.views import PsicologoModelViewSet
from paciente.views import PacienteModelViewSet

router = routers.DefaultRouter()

router.register(r'psicologos', PsicologoModelViewSet)

psicologo_router = routers.NestedDefaultRouter(
    router,
    r'psicologos',
    lookup='psicologo'
)

psicologo_router.register(r'pacientes', PacienteModelViewSet)

# router.registry.extend(psicologo_router.registry)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(psicologo_router.urls)),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', include('users.urls')),
    # path('api/register/', include('users.urls')),
]
