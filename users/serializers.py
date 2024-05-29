from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from users.models import Payments, User, Subscription


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PaymentsSerializer(ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('course',)


class SubscriptionResponse(serializers.Serializer):
    message = serializers.CharField()
