from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime as dt

def first(request):
    d = {
        'date':dt.now().strftime('%Y/%m/%d')
    }
    return render(request, 'first.html',d)
