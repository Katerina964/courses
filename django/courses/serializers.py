from rest_framework import serializers
from courses.models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = ['name', 'description', 'start_date', 'end_date', ]
