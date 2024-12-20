from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    return HttpResponse('<h1>The first html tag of the task</h1><h2>The second html tag of the task</h2>')

# Create your views here.
