from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateAPIView, LessonRetrieveAPIView, LessonListAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view()),
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='create'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='read'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view()),
              ] + router.urls
