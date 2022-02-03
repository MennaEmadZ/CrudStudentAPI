from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greeting(request,name):
    
    return HttpResponse('<h1><center>hello {}</center></h1>'.format(name))