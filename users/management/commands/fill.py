from datetime import datetime

from django.core.management import BaseCommand

from lms.models import Course, Lesson
from users.models import Payments, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()
        Payments.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()

        user_list = [
            {
                'email': 'test1@sky.ru'
            },
            {
                'email': 'test2@sky.ru'
            },
            {
                'email': 'test3@sky.ru'
            }
        ]

        user_for_create = []
        for user in user_list:
            user_for_create.append(User(**user))
        User.objects.bulk_create(user_for_create)

        course_list = [
            {
                'name': 'Энергетика'
            },
            {
                'name': 'Механика'
            },
            {
                'name': 'Химанализ'
            }
        ]

        course_for_create = []
        for course in course_list:
            course_for_create.append(Course(**course))
        Course.objects.bulk_create(course_for_create)

        lesson_list = [
            {
                'name': 'Электротехника',
                'course': course_for_create[0]
            },
            {
                'name': 'Физика',
                'course': course_for_create[1]
            },
            {
                'name': 'Химия',
                'course': course_for_create[2]

            }
        ]
        lesson_for_create = []
        for lesson in lesson_list:
            lesson_for_create.append(Lesson(**lesson))
        Lesson.objects.bulk_create(lesson_for_create)

        payments_list = [
            {
                'user': user_for_create[0],
                'pay_day': datetime.now().date,
                'course_pay': course_for_create[0],
                'lesson_pay': lesson_for_create[0],
                'sum_pay': 15000,
                'pay_method': 'Наличные'
            },
            {
                'user': user_for_create[1],
                'pay_day': datetime.now().date,
                'course_pay': course_for_create[1],
                'lesson_pay': lesson_for_create[1],
                'sum_pay': 12000,
                'pay_method': 'Перевод на счет'
            },
            {
                'user': user_for_create[2],
                'pay_day': datetime.now().date,
                'course_pay': course_for_create[2],
                'lesson_pay': lesson_for_create[2],
                'sum_pay': 10000,
                'pay_method': 'Наличные'
            }
        ]

        payments_for_create = []
        for payment in payments_list:
            payments_for_create.append(Payments(**payment))
        Payments.objects.bulk_create(payments_for_create)
