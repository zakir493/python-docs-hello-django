from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hi HPE Team good evening, Today - Monday , Its evening, We are learning AZURE Cloud Computing[AZ900] & its very very interesting :-) ~!! ")
