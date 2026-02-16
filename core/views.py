from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import StudentProfile, Mark, Timetable, Attendance



def home(request):
    return HttpResponse("Tuition Management System – Student Portal")

def student_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return HttpResponse("Invalid username or password")

    return render(request, "core/login.html")

@login_required(login_url="/login/")
def dashboard(request):
    return render(request, "core/dashboard.html")

def student_logout(request):
    logout(request)
    return redirect("login")
def home(request):
    return render(request, "core/home.html")
@login_required(login_url="/login/")
def dashboard(request):
    try:
        student = StudentProfile.objects.get(user=request.user)
    except StudentProfile.DoesNotExist:
        return HttpResponse("Student profile not found. Contact admin.")

    marks = Mark.objects.filter(student=student)
    timetable = Timetable.objects.filter(student=student)
    attendance = Attendance.objects.filter(student=student)

    # Subject-wise grade calculation
    subject_results = []

    for m in marks:
        percent = round((m.marks_obtained / m.max_marks) * 100, 2)


        if percent >= 90:
            grade = "A+"
        elif percent >= 80:
            grade = "A"
        elif percent >= 70:
            grade = "B+"
        elif percent >= 60:
            grade = "B"
        elif percent >= 50:
            grade = "C+"
        elif percent >= 40:
            grade = "C"
        elif percent >= 30:
            grade = "D+"
        else:
            grade = "Fail"


        subject_results.append({
            "subject": m.subject.name,
            "obtained": m.marks_obtained,
            "max": m.max_marks,
            "percentage": percent,
            "grade": grade,
        })

    is_new_student = len(subject_results) == 0

    return render(request, "core/dashboard.html", {
        "student": student,
        "subject_results": subject_results,
        "timetable": timetable,
        "attendance": attendance,
        "is_new_student": is_new_student,
    })


def student_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        roll_number = request.POST.get("roll_number")
        class_name = request.POST.get("class_name")

        if User.objects.filter(username=username).exists():
            return render(request, "core/register.html", {
                "error": "Username already exists"
            })

        if StudentProfile.objects.filter(roll_number=roll_number).exists():
            return render(request, "core/register.html", {
                "error": "Roll number already registered"
            })

        user = User.objects.create_user(
            username=username,
            password=password
        )

        StudentProfile.objects.create(
            user=user,
            roll_number=roll_number,
            class_name=class_name
        )

        login(request, user)
        return redirect("dashboard")

    return render(request, "core/register.html")

