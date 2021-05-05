from django.contrib import admin
from django.urls import path, include
# from paciente.views import PacienteViewSet
from rest_framework_nested import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view
from users.views import PsicologoModelViewSet
from paciente.views import PacienteModelViewSet, ConsultaModelViewSet
from rest_framework.documentation import include_docs_urls
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

# psicologo_router.register(r'consultas', ConsultaModelViewSet)

# router.registry.extend(psicologo_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/', include(psicologo_router.urls)),
    path('api/', include(paciente_router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', include('users.urls')),
    path('docs/', include_docs_urls(title='CheerUP')),
    path('schema', get_schema_view(
        title="CheerUP",
        description="Api da pagina web CheeryUp ",
        version="1.0.0"
    ), name='openapi-schema'),
    # path('api/register/', include('users.urls')),
]
