from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    def get_student(self):
        students = CourseParticipant.objects.filter(course=self.pk)
        number = students.count()
        list_students = [number]
        for each in students:
            list_students.append(f"{each.student.first_name} {each.student.last_name}")

        return list_students

    class Meta:
        ordering = ['start_date']


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()


class CourseParticipant(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    completed = models.BooleanField(default="False")
