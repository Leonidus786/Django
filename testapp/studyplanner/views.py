from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to Abhishek Study TimeTable")

def monday(request):
    return HttpResponse("Today I'll be studying C++")

def tuesday(request):
    return HttpResponse("Today I'll be studying Data Science")

def wednesday(request):
    return HttpResponse("Today I'll be studying Machine Learning")

def thursday(request):
    return HttpResponse("Today I'll be studying Statistic")

def friday(request):
    return HttpResponse("Today I'll be studying Linear Algebra")

def saturday(request):
    return HttpResponse("Today I'll be studying SQL")

def sunday(request):
    return HttpResponse("Ab aaj to kch ni pdhunga")