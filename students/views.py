from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def students(request):
    students = [
        {'id': 1,'name':'suraj','age':25}
    ]
    return HttpResponse(students)