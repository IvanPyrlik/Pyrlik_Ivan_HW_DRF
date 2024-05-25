from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from lms.models import Course
from users.models import User


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Создание тест пользователя.
        self.user = User.objects.create(id=1, email='user1@test.ru', password='123',)
        self.client.force_authenticate(user=self.user)

        # Создание тест курса.
        self.course = Course.objects.create(name='test_course', description='test_description')

        # Ссылка на подписку.
        self.path = reverse('users:sub', [self.course.id])

    def test_sub_on(self):
        """
        Тестрование добавления подписки.
        """
        response = self.client.post(self.path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Подписка добавлена")

    def test_sub_off(self):
        """
        Тестрование удаления подписки.
        """
        response = self.client.post(self.path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Подписка удалена")
