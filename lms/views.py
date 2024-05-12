from rest_framework.viewsets import ModelViewSet

from lms.models import Course, Lesson
from lms.serializers import CourseSerializer, LessonSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListApiView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCreateApiView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailApiView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateApiView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDeleteApiView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
