from rest_framework import serializers

from users.models import Payment


# Create your views here.

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
