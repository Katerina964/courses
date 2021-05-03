from rest_framework import serializers
from courses.models import Course, CourseParticipant, Student


class CourseSerializer(serializers.ModelSerializer):
    student = serializers.ListField(source="get_student")

    class Meta:
        model = Course
        fields = ['name', 'description', 'start_date', 'end_date', 'student']


class CourseParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseParticipant
        fields = ['course', 'student', 'completed']


class StudentSerializer(serializers.ModelSerializer):
    number = serializers.ListField(source="report")

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'number']
