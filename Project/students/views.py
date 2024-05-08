from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Student
from .forms import NameForm, StudentForm
from django.urls import reverse


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


def get_name(request):
    template = loader.get_template('name.html')
    if request.method == "POST":
        form = NameForm(request.POST)

        if form.is_valid():
            named = form.cleaned_data['your_name']
            # print(named)

            url = reverse("showName", kwargs={'named': named})

            return HttpResponseRedirect(url)

    else:
        form = NameForm()

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def show_name(request, named):
    template = loader.get_template('show_name.html')
    context = {
        'named': named,
    }

    return HttpResponse(template.render(context, request))


def new_user(request):
    template = loader.get_template('new_user.html')
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            birthday = form.cleaned_data['birthday']
            studentId = form.cleaned_data['studentID']
            phone = form.cleaned_data['phone']

            student = Student(firstname=firstname, lastname=lastname,
                              birthday=birthday, studentID=studentId,
                              phone=phone)
            print(student)
            student.save()

            return HttpResponseRedirect("/list/")

    else:
        form = StudentForm()

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))

