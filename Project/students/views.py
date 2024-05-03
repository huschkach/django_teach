from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student


# Create your views here.
def students(request):
    template = loader.get_template('hello_matrix.html')
    return HttpResponse(template.render())


def student_list(request):
    mystudents = Student.objects.all().values()
    template = loader.get_template('student_list.html')
    context = {
        'mystudents': mystudents,
    }
    return HttpResponse(template.render(context, request))


def lebenslauf(request):
    template = loader.get_template('lebenslauf.html')
    return HttpResponse(template.render())
