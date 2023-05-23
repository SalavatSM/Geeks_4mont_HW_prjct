from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')
