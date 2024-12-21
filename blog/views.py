from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_coffee(request):
    return HttpResponse("have a Joe!")
