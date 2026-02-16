from django.contrib import admin
from .models import StudentProfile, Subject, Mark,Timetable,Attendance

admin.site.register(StudentProfile)
admin.site.register(Subject)
admin.site.register(Mark)
admin.site.register(Timetable)
admin.site.register(Attendance)
