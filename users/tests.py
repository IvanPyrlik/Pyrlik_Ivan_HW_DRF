from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from lms.models import Course
from users.models import User, Subscription


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Создание тест пользователя.
        self.user = User.objects.create(id=1, email='user1@test.ru', password='123')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(name='test_course', description='test_description', owner=self.user)
        self.subscription = Subscription.objects.create(course=self.course, user=self.user)

        self.path = reverse('users:sub', [self.user], [self.course])

    def test_sub_on(self):
        """
        Тестрование добавления подписки.
        """
        response = self.client.post(self.path)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Подписка добавлена")

    def test_sub_off(self):
        """
        Тестрование удаления подписки.
        """
        response = self.client.post(self.path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['message'], "Подписка удалена")
