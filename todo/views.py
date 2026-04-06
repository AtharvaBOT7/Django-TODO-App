from django.shortcuts import render
from django.http import HttpResponse

def addTask(request):
    return HttpResponse("Add Task")