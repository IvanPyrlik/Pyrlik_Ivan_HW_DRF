from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course/images', verbose_name='Картинка', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название урока')
    preview = models.ImageField(upload_to='lesson/images', verbose_name='Картинка', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    video_url = models.URLField(max_length=200, verbose_name='Ссылка на видео', **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Название курса', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
