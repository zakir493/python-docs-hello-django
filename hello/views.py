from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hi Team, We are learning HCI & its very interesting ~!! ")
