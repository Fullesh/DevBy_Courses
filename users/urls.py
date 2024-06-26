from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateView, UserDestroyAPIView, \
    PaymentsListAPIView, PaymentsCreateAPIView, MyTokenObtainPairView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('view/<int:pk>', UserRetrieveAPIView.as_view(), name='user_view'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>', UserDestroyAPIView.as_view(), name='user_delete'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("payments/create/", PaymentsCreateAPIView.as_view(), name="payments-create"),
    path('payments/list/', PaymentsListAPIView.as_view(), name='payments-list'),
]
