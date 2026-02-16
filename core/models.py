from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Subject(models.Model):
    name = models.CharField(max_length=100)
    max_marks = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Out of {self.max_marks})"


class Mark(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    max_marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.user.username} - {self.subject.name}"

class Timetable(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.user.username} - {self.day}"
class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent')
        ]
    )

    def __str__(self):
        return f"{self.student.user.username} - {self.date} - {self.status}"


