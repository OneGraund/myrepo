from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

def index(request):
    return HttpResponse('Welcome to home page')