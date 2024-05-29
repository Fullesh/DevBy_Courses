from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lession, Subscription
from materials.paginators import LessionPaginator, CoursePaginator
from materials.permissions import IsModerator, IsOwner
from materials.serializers import CourseSerializer, LessionSerializer, SubscriptionSerializer


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


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        print(self.request.data.get('id'))
        course = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.all().filter(user=user).filter(course=course).first()

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка отключена'
        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Подписка включена'
        return Response({"message": message})
