from courses.models import Course, CourseParticipant, Student
from courses.serializers import CourseSerializer, CourseParticipantSerializer, StudentReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from rest_framework import status


class CourseList(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class ParticipantCreate(APIView):
    def get(self, request, format=None):
        participant = CourseParticipant.objects.all()
        serializer = CourseParticipantSerializer(participant, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParticipantDelete(APIView):
    def get_object(self, pk):
        try:
            return CourseParticipant.objects.get(pk=pk)
        except CourseParticipant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        participant = self.get_object(pk)
        serializer = CourseParticipantSerializer(participant)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        participant = self.get_object(pk)
        participant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentReport(APIView):
    renderer_classes = (r.CSVRenderer, ) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentReportSerializer(student)
        return Response(serializer.data)
