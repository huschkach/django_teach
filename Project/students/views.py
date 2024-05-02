from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def students(request):
    template = loader.get_template('hello_matrix.html')
    return HttpResponse(template.render())
