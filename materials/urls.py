from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessionListAPIView, LessionCreateAPIView, LessionRetieveAPIView, \
    LessionUpdateAPIView, LessionDestroyAPIView
from users.views import PaymentViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register('payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('lessions/', LessionListAPIView.as_view(), name='lession_view'),
    path('lessions/create/', LessionCreateAPIView.as_view(), name='lession_create'),
    path('lessions/<int:pk>/', LessionRetieveAPIView.as_view(), name='lession_detail'),
    path('lessions/update/<int:pk>/', LessionUpdateAPIView.as_view(), name='lession_update'),
    path('lessions/delete/<int:pk>/', LessionDestroyAPIView.as_view(), name='lession_delete'),
] + router.urls
