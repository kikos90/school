from .models import *
from django.shortcuts import render


def index(request):
    school = School.objects.all()
    director = Director.objects.all()
    headteachder = HeadTeacher.objects.all()
    teacher = Teacher.objects.all()
    students = Students.objects.all()
    context = {
        'school' : school,
        'director' : director,
        'headteacher' : headteachder,
        'teacher' : teacher,
        'pupil' : students,
    }

    return render(request, template_name='blog/index.html', context=context)