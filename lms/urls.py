from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, CourseListApiView, CourseDetailApiView, CourseCreateApiView, CourseUpdateApiView, \
    CourseDeleteApiView, LessonViewSet, LessonListApiView, LessonDetailApiView, LessonCreateApiView, \
    LessonUpdateApiView, LessonDeleteApiView

router = SimpleRouter()
router.register('', CourseViewSet, basename='course')
router.register('', LessonViewSet, basename='lesson')

app_name = LmsConfig.name

urlpatterns = [
                  path('course/', CourseListApiView.as_view(), name='course-list'),
                  path('course/<int:pk>/', CourseDetailApiView.as_view(), name='course-detail'),
                  path('course/create/', CourseCreateApiView.as_view(), name='course-create'),
                  path('course/update/<int:pk>/', CourseUpdateApiView.as_view(), name='course-update'),
                  path('course/delete/<int:pk>/', CourseDeleteApiView.as_view(), name='course-delete'),
                  path('lesson/', LessonListApiView.as_view(), name='lesson-list'),
                  path('lesson/<int:pk>/', LessonDetailApiView.as_view(), name='lesson-detail'),
                  path('lesson/create/', LessonCreateApiView.as_view(), name='lesson-create'),
                  path('lesson/update/<int:pk>/', LessonUpdateApiView.as_view(), name='lesson-update'),
                  path('lesson/delete/<int:pk>', LessonDeleteApiView.as_view(), name='lesson-delete'),
              ] + router.urls
