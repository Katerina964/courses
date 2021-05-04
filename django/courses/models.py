from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.last_name


class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(Student, through="CourseParticipant", through_fields=("course", "student"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['start_date']


class CourseParticipant(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
