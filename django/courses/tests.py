from django.test import TestCase
from .models import Student, Course, CourseParticipant
from django.urls import reverse


class CourseGoTests(TestCase):
    print("ПОЕХАЛИ")
    print()

    @classmethod
    def setUpTestData(cls):
        student = Student.objects.create(first_name="Коля", last_name="Федоров", email="nicolay@gmail.com")
        course = Course.objects.create(name="Python", description="all", start_date="2020-05-01", end_date='2020-05-03')
        CourseParticipant.objects.create(course=course, student=student)

    def test_courses(self):
        response = self.client.get(reverse('courses:list'))
        self.assertEqual(response.status_code, 200,)
        print(response.data)
        data = {
                "name": "Python",
                "description": "all",
                "start_date": "2020-05-01",
                "end_date": "2020-05-03",
                "students_count": 1,
                "students": [
                    {
                     "first_name": "Коля",
                     "last_name": "Федоров"
                    }, ]}

        self.assertEqual(dict(response.data[0]), data)
        self.assertEqual(len(response.data), 1)

    def test_create(self):
        response = self.client.get(reverse('courses:create'))
        self.assertEqual(response.status_code, 200,)

    def test_report(self):
        report = Student.objects.get(id=1)
        response = self.client.get(reverse('courses:report', args=[report.id]))
        data = {'first_name': 'Коля', 'last_name': 'Федоров', 'courses_count': 1, 'completed_courses_count': 0}
        print(response.data)
        self.assertEqual(response.status_code, 200, )
        self.assertEqual(dict(response.data), data)
        self.assertEqual(len(response.data), 4)

    def test_delete(self):
        participant = CourseParticipant.objects.get(pk=1)
        response = self.client.get(reverse('courses:delete', args=[participant.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
