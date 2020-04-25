from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, num1, num2):
    tot = int(num1) + int(num2)
    return HttpResponse('O total é: {}'.format(tot))

