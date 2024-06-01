from rest_framework import serializers

from materials.models import Course, Lession, Subscription
from materials.validators import URLValidator


class LessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lession
        fields = '__all__'
        validators = [URLValidator(url='URL')]


class CourseSerializer(serializers.ModelSerializer):
    lession = LessionSerializer(source='lession_set', many=True, read_only=True)
    lessions_quantity = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_subscription(self, instance):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=instance).exists()

    def get_lessions_quantity(self, instance):
        if instance.lession_set.all():
            return instance.lession_set.count()
        return 0

    def create(self, validated_data):
        lession = validated_data.pop('lession_set')

        course_item = Course.objects.create(**validated_data)

        for l in lession:
            Lession.objects.create(**l, course=course_item)

        return course_item


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
