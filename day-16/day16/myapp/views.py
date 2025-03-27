from django.shortcuts import render, redirect, get_object_or_404
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


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(reverse('student_list'))  # Redirect to list after updating
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect(reverse('student_list'))  # Redirect to list after deletion
    return render(request, 'delete_student.html', {'student': student})