from rest_framework import serializers
from courses.models import Course, CourseParticipant, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']


class CourseSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['name', 'description', 'start_date', 'end_date', 'students_count', 'students']

    def get_students_count(self, obj):
        return obj.students.count()

    def get_students(self, obj):
        students = Student.objects.filter(courseparticipant__course=obj.id)[:10]
        serializer = StudentSerializer(instance=students, many=True)
        return serializer.data


class StudentReportSerializer(serializers.ModelSerializer):
    courses_count = serializers.SerializerMethodField()
    completed_courses_count = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'courses_count', 'completed_courses_count']

    def get_courses_count(self, obj):
        return Course.objects.filter(courseparticipant__student=obj.id).count()

    def get_completed_courses_count(self, obj):
        return Course.objects.filter(courseparticipant__student=obj.id, courseparticipant__completed=True).count()


class CourseParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseParticipant
        fields = ['course', 'student', 'completed']
