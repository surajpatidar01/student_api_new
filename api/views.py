from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def studentsView(request):
    students = {
        'id':1,
        'name':'suraj',
        'age':24
    }
    return JsonResponse(students)