from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.authtoken.views import obtain_auth_token
from users.views import PsicologoModelViewSet
from paciente.views import PacienteModelViewSet, ConsultaModelViewSet, getGender, getPacienteGraphEvolution
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()

router.register(r'psicologos', PsicologoModelViewSet)

psicologo_router = routers.NestedDefaultRouter(
    router,
    r'psicologos',
    lookup='psicologo'
)

psicologo_router.register(r'pacientes', PacienteModelViewSet)


paciente_router = routers.NestedSimpleRouter(psicologo_router, r'pacientes', lookup='paciente')

paciente_router.register(r'consultas', ConsultaModelViewSet, basename='consultas')

schema_view = get_schema_view(
   openapi.Info(
      title="CheeryUp",
      default_version='v1',
      description="Documentação do grupo 7 de MDS-CheryUp",
      terms_of_service="https://fga-eps-mds.github.io/2020.2-CheeryUP/#/./wiki/CONTRIBUTING",
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/', include(psicologo_router.urls)),
    path('api/', include(paciente_router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/psicologos/<user__username>/pacientes/getGender', getGender, name='get_gender'),
    path('api/psicologos/<user__username>/pacientes/<cpf>/getGraphEvolution', getPacienteGraphEvolution, name='get_graph_evolution')
]
