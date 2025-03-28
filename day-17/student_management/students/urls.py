from django.urls import path
from .views import home, student_list, add_student, update_student, delete_student

urlpatterns = [
    path('', home, name='home'),  # Homepage
    path('list/', student_list, name='student_list'),
    path('add/', add_student, name='add_student'),
    path('update/<int:id>/', update_student, name='update_student'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
]
