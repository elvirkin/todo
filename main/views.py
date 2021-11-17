from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("Добро пожаловать в приложение ToDo-Admin")

def test(request):
    return render(request,"test.html")