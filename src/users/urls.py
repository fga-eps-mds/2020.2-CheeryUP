from django.urls import path
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
