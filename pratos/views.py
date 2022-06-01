from django.shortcuts import render
from django.http import HttpResponse

def pratos(request):
    return HttpResponse('<h1>Vai dar certo é de primeira!!!</h1>')