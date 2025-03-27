from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.urls import reverse

def student_list(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('student_list'))  # Redirect to list after adding
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})
