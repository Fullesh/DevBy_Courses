from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessionListAPIView, LessionCreateAPIView, LessionRetieveAPIView, \
    LessionUpdateAPIView, LessionDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')

urlpatterns = [
    path('lessions/', LessionListAPIView.as_view(), name='lession_view'),
    path('lessions/create/', LessionCreateAPIView.as_view(), name='lession_create'),
    path('lessions/<int:pk>/', LessionRetieveAPIView.as_view(), name='lession_detail'),
    path('lessions/update/<int:pk>/', LessionUpdateAPIView.as_view(), name='lession_update'),
    path('lessions/delete/<int:pk>/', LessionDestroyAPIView.as_view(), name='lession_delete'),
] + router.urls
