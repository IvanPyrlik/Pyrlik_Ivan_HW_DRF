from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from yaml import serializer

from users.models import Payments, User, Subscription
from users.serializers import PaymentsSerializer, UserSerializer, SubscriptionSerializer, SubscriptionResponse
from users.services import convert_rub_to_dollars, create_stripe_product, create_stripe_price, create_stripe_sessions


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentsListApiView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    search_fields = ('course_pay', 'lesson_pay', 'pay_method',)
    ordering_fields = ('pay_day',)


class PaymentsCreateApiView(CreateAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        amount_in_dollars = convert_rub_to_dollars(payment.amount)
        product = create_stripe_product(payment)
        price = create_stripe_price(amount_in_dollars, product)
        session_link, session_id = create_stripe_sessions(price)
        payment.pay_link = session_link
        payment.session_id = session_id
        payment.save()


class SubscriptionApiView(APIView):
    permission_classes = [IsAuthenticated]


    @swagger_auto_schema(
        request_body=SubscriptionSerializer,
        responses={
            201: SubscriptionResponse(),
            204: SubscriptionResponse(),
        }
    )

    def post(self, *args, **kwargs):
        user = self.request.user
        course = serializer.validated_data['course']

        sub_item = Subscription.objects.filter(user=user, course=course)

        if sub_item.exists():
            sub_item.delete()
            message = 'Подписка удалена'
            status_code = status.HTTP_204_NO_CONTENT
        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Подписка добавлена'
            status_code = status.HTTP_201_CREATED

        return Response({'message': message}, status=status_code)
