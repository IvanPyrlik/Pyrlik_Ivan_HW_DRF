from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonListApiView, LessonDetailApiView, LessonCreateApiView, \
    LessonUpdateApiView, LessonDeleteApiView

router = SimpleRouter()
router.register('', CourseViewSet, basename='course')

app_name = LmsConfig.name

urlpatterns = [
                  path('lesson/', LessonListApiView.as_view(), name='lesson-list'),
                  path('lesson/<int:pk>/', LessonDetailApiView.as_view(), name='lesson-detail'),
                  path('lesson/create/', LessonCreateApiView.as_view(), name='lesson-create'),
                  path('lesson/update/<int:pk>/', LessonUpdateApiView.as_view(), name='lesson-update'),
                  path('lesson/delete/<int:pk>', LessonDeleteApiView.as_view(), name='lesson-delete'),
              ] + router.urls
