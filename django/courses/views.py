from courses.models import Course, CourseParticipant, Student
from courses.serializers import CourseSerializer, CourseParticipantSerializer, StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
# from rest_framework import mixins
# from rest_framework import generics
from rest_framework import viewsets


class CourseList(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class ParticipantCreateDelete(viewsets.ModelViewSet):
    queryset = CourseParticipant.objects.all()
    serializer_class = CourseParticipantSerializer
    http_method_names = ['post', 'get', 'delete']


class StudentReport(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
