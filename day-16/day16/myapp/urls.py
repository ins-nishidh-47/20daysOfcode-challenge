from django.urls import path
from .views import student_list, add_student, update_student, delete_student

urlpatterns = [
    path('', student_list, name='student_list'),  # Home page with student list
    path('add/', add_student, name='add_student'),  # Form to add student
    path('update/<int:student_id>/', update_student, name='update_student'),
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
]
