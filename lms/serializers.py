from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson
from lms.validators import URLValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(fields=['description', 'video_url'])]


class CourseSerializer(ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        validators = [URLValidator(fields=['description'])]


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, course):
        return Course.objects.filter(lesson=course.lesson).count()

    class Meta:
        model = Course
        fields = ('name', 'count_lessons',)
