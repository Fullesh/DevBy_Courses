from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from materials.models import Course, Lession
from materials.paginators import LessionPaginator, CoursePaginator
from materials.permissions import IsModerator, IsOwner
from materials.serializers import CourseSerializer, LessionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated | IsAdminUser]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated | IsModerator | IsOwner]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAuthenticated | IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated | IsAdminUser | IsOwner]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated | IsOwner | IsAdminUser]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated | IsOwner | IsAdminUser]
        return [permission() for permission in self.permission_classes]


class LessionCreateAPIView(generics.CreateAPIView):
    serializer_class = LessionSerializer
    permission_classes = [IsAuthenticated | IsAdminUser | IsOwner]

    def perform_create(self, serializer):
        new_lession = serializer.save()
        new_lession.owner = self.request.user
        new_lession.save()


class LessionListAPIView(generics.ListAPIView):
    serializer_class = LessionSerializer
    queryset = Lession.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]
    pagination_class = LessionPaginator


class LessionRetieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessionSerializer
    queryset = Lession.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessionSerializer
    queryset = Lession.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessionDestroyAPIView(generics.DestroyAPIView):
    queryset = Lession.objects.all()
    permission_classes = [IsAuthenticated | IsAdminUser | IsOwner]
