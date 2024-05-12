from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, course):
        return Course.objects.filter(lesson=course.lesson).count()

    class Meta:
        model = Course
        fields = ('name', 'count_lessons',)
