from django.http import HttpResponse

#def Hi(request):
    #return HttpResponse("Hello, Django! I am Lamborghini.")

def hello1(request):
    return HttpResponse("Hello world ! ")

from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

