from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Base home')

def room(request):
    return HttpResponse('Base room')