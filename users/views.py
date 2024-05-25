from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course
from users.models import Payments, User, Subscription
from users.serializers import PaymentsSerializer, UserSerializer, SubscriptionSerializer


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


class SubscriptionApiView(APIView):

    serializer_class = SubscriptionSerializer

    def post(self, request, pk):
        queryset = Course.objects.filter(pk=pk)
        user = self.request.user
        course = get_object_or_404(queryset=queryset)
        sub_item = Subscription.objects.filter(course=course, user=user)

        if sub_item.exists():
            sub_item.delete()
            message = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course)
            message = 'Подписка добавлена'

        return Response({'message': message})
