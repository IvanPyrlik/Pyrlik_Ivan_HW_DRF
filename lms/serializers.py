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
    count_lessons = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_count_lessons(self, obj) -> int:
        return obj.lesson.all().count()

    class Meta:
        model = Course
        fields = ['name', 'description', 'preview', 'count_lessons', 'lesson']
        validators = [URLValidator(fields=['description'])]


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons_list = SerializerMethodField()
    is_subscribed = SerializerMethodField()

    def user_(self):
        request = self.context.get('request', None)
        if request:
            return request.user
        return None

    def get_is_subscribed(self, course) -> bool:
        return course.subscription_set.filter(user=self.user_()).exists()

    def get_count_lessons(self, course) -> int:
        return Lesson.objects.filter(course=course).count()

    def get_lessons_list(self, course) -> list:
        return LessonSerializer(Lesson.objects.filter(course=course), many=True).data

    class Meta:
        model = Course
        fields = '__all__'
