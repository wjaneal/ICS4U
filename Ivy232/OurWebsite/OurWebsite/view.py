
from django.http import HttpResponse
 
from django.shortcuts import render

def hello(request):
    context          = {}

    return render(request, 'hello.html', context)

