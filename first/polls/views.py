from django.http import HttpResponse
from django.shortcuts import render

def index(requeet):
    return HttpResponse("polls index")