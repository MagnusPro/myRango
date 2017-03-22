from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'message': 'I AM RANGO'}
    return render(request,'rango/index.html',context)

def about(request):
    context = {'message': "This is about!"}
    return render(request, 'rango/about.html', context)