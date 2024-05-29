from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateApiView, SubscriptionApiView, PaymentsListApiView, PaymentsCreateApiView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('sub/', SubscriptionApiView.as_view(), name='sub'),
    path('payments/create/', PaymentsCreateApiView.as_view(), name='payments_create'),
    path('payments/', PaymentsListApiView.as_view(), name='payments_list'),
]
