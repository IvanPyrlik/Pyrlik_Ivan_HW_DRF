from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=11, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='Страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments', verbose_name='Пользователь',
                             **NULLABLE)
    pay_day = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты', **NULLABLE)
    course_pay = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments',
                                   verbose_name='Оплаченный курс', **NULLABLE)
    lesson_pay = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payments',
                                   verbose_name='Оплаченный урок', **NULLABLE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    pay_method = models.CharField(max_length=100, verbose_name='Способ оплаты', **NULLABLE)

    pay_link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', **NULLABLE)
    session_id = models.CharField(max_length=255, verbose_name='ID Сессии', **NULLABLE)

    def __str__(self):
        return f'{self.user} - сумма оплаты: {self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('user', 'pay_day',)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Название курса')

    def __str__(self):
        return f'{self.user} - подписка: {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
