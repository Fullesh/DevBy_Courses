from rest_framework import serializers

from materials.models import Course, Lession


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class LessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lession
        fields = '__all__'