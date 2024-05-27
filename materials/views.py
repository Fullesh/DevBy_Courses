from rest_framework import viewsets, generics

from materials.models import Course, Lession
from materials.serializers import CourseSerializer, LessionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessionCreateAPIView(generics.CreateAPIView):
    serializer_class = LessionSerializer


class LessionListAPIView(generics.ListAPIView):
    serializer_class = LessionSerializer
    queryset = Lession.objects.all()


class LessionRetieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessionSerializer
    queryset = Lession.objects.all()


class LessionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessionSerializer
    queryset = Lession.objects.all()


class LessionDestroyAPIView(generics.DestroyAPIView):
    queryset = Lession.objects.all()
