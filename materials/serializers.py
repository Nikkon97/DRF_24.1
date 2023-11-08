from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'pk',
            'course',
            'title',
            'description',
            'video_link'
        )

        validators = [LinkValidator(field='title')]


class LessonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'pk',
            'title',
        )


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    # lessons = LessonInfoSerializer(source='lesson_set', many=True)
    has_subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'pk',
            'title',
            'description',
            'lesson_count',
            # 'lessons',
            'has_subscription'
        )

    def _user(self):
        if self.context.get('request'):
            self.context['request'].user
        return None

    def get_has_subscription(self, instance):
        return instance.subscription_set.filter(user=self._user()).exists()

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()
