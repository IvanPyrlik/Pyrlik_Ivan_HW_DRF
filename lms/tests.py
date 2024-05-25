from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from lms.models import Course, Lesson
from users.models import User


class LessonAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        # Создание тест пользователя.
        self.user = User.objects.create(id=1, email='user1@test.ru', password='123')
        self.client.force_authenticate(user=self.user)

        # Создание тестовых курса и урока.
        self.course = Course.objects.create(name='test_course', description='test_description')
        self.lesson = Lesson.objects.create(name='test_lesson',
                                            description='test_description',
                                            course=self.course,
                                            video_url='https://test.youtube.com/',
                                            owner=self.user)

    def test_create_lesson(self):
        """
        Тестирование создания урока.
        """
        data = {'name': 'test_create', 'description': 'test_create',
                'course': self.course.id, 'video_url': 'https://test.youtube.com/',
                'owner': self.user.id}
        response = self.client.post('/lesson/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Lesson.objects.filter(name=data['name']).exists())

    def test_detail_lesson(self):
        """
        Тестирование просмотра информации об уроке.
        """
        path = reverse('lms:lesson-detail', [self.lesson.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.lesson.name)

    def test_update_lesson(self):
        """
        Тестирование редактирования урока.
        """
        path = reverse('lms:lesson-update', [self.lesson.pk])
        data = {'name': 'test_update', 'description': 'test_update'}
        response = self.client.patch(path, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.name, data['name'])

    def test_delete_lesson(self):
        """
        Проверка на права доступа.
        """
        moder = User.objects.create(id=2, email='moder@test.ru', password='345')
        self.client.force_authenticate(user=moder)

        path = reverse('lms:lesson-delete', [self.lesson.id])
        response = self.client.delete(path)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
