from rest_framework import serializers

from materials.models import Course, Lession


class LessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lession
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lession = LessionSerializer(source='lession_set', many=True)
    lessions_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessions_quantity(self, instance):
        if instance.lession_set.all():
            return instance.lession_set.count()
        return 0
