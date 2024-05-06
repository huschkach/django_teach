from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Student


# Create your views here.
def students(request):
    template = loader.get_template('hello_matrix.html')
    return HttpResponse(template.render())


def student_list(request):
    # SELECT firstname, lastname, birthday, studentId, phone  FROM Student;
    mystudents = Student.objects.all().values()
    template = loader.get_template('student_list.html')
    context = {
        'mystudents': mystudents,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mystudent = get_object_or_404(Student, studentID=id)
    template = loader.get_template('details_student.html')
    context = {
        'mystudent': mystudent,
    }
    return HttpResponse(template.render(context, request))


def lebenslauf(request):
    template = loader.get_template('lebenslauf.html')
    return HttpResponse(template.render())

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
