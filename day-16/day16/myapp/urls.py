from django.urls import path
from .views import student_list, add_student

urlpatterns = [
    path('', student_list, name='student_list'),  # Home page with student list
    path('add/', add_student, name='add_student'),  # Form to add student
]
