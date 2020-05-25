from django.shortcuts import render
from django.http import HttpResponse
def show2(request):
    return HttpResponse("hello world!")

def login(request):
    return HttpResponse('login page')

